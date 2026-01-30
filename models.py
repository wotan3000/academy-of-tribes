"""
AoT (Academy of Tribes) - Database Models
SQLAlchemy models for users, assessments, and results
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json
import uuid

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """User account model"""
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    display_name = db.Column(db.String(100))
    avatar_url = db.Column(db.String(500))
    bio = db.Column(db.Text)

    # Profile settings
    is_public = db.Column(db.Boolean, default=False)
    show_results = db.Column(db.Boolean, default=True)
    email_notifications = db.Column(db.Boolean, default=True)
    theme = db.Column(db.String(20), default='dark')

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    # Gamification
    xp_points = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=1)
    streak_days = db.Column(db.Integer, default=0)
    last_activity = db.Column(db.Date)

    # Relationships
    results = db.relationship('AssessmentResult', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    badges = db.relationship('UserBadge', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    teams = db.relationship('TeamMember', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    insights = db.relationship('PersonalityInsight', backref='user', lazy='dynamic', cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add_xp(self, points):
        """Add XP and check for level up"""
        self.xp_points += points
        new_level = self.calculate_level()
        leveled_up = new_level > self.level
        self.level = new_level
        return leveled_up

    def calculate_level(self):
        """Calculate level based on XP (exponential scaling)"""
        # Level formula: XP needed = 100 * level^1.5
        level = 1
        xp_needed = 0
        while xp_needed <= self.xp_points:
            level += 1
            xp_needed += int(100 * (level ** 1.5))
        return level - 1

    def get_primary_type(self, assessment_type='mbti'):
        """Get user's most recent result for an assessment type"""
        result = self.results.filter_by(assessment_type=assessment_type).order_by(
            AssessmentResult.created_at.desc()
        ).first()
        return result.result_type if result else None

    def to_dict(self, include_private=False):
        data = {
            'id': self.id,
            'username': self.username,
            'display_name': self.display_name or self.username,
            'avatar_url': self.avatar_url,
            'bio': self.bio,
            'level': self.level,
            'xp_points': self.xp_points,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_public': self.is_public,
        }
        if include_private:
            data.update({
                'email': self.email,
                'theme': self.theme,
                'email_notifications': self.email_notifications,
                'streak_days': self.streak_days,
            })
        return data


class AssessmentResult(db.Model):
    """Store assessment results"""
    __tablename__ = 'assessment_results'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=True, index=True)

    # Assessment info
    assessment_type = db.Column(db.String(50), nullable=False, index=True)  # mbti, big5, enneagram, disc, cognitive
    result_type = db.Column(db.String(50), nullable=False)  # e.g., "INTJ", "5w4", "DC"

    # Detailed scores (JSON)
    scores = db.Column(db.Text)  # JSON string of detailed scores
    percentages = db.Column(db.Text)  # JSON string of percentages
    answers = db.Column(db.Text)  # JSON string of original answers

    # Metadata
    time_taken = db.Column(db.Integer)  # seconds
    is_public = db.Column(db.Boolean, default=False)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    def get_scores(self):
        return json.loads(self.scores) if self.scores else {}

    def get_percentages(self):
        return json.loads(self.percentages) if self.percentages else {}

    def set_scores(self, scores_dict):
        self.scores = json.dumps(scores_dict)

    def set_percentages(self, pct_dict):
        self.percentages = json.dumps(pct_dict)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'assessment_type': self.assessment_type,
            'result_type': self.result_type,
            'scores': self.get_scores(),
            'percentages': self.get_percentages(),
            'time_taken': self.time_taken,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


class Badge(db.Model):
    """Badge definitions"""
    __tablename__ = 'badges'

    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(50))  # emoji or icon class
    category = db.Column(db.String(50))  # achievement, streak, social, etc.
    xp_reward = db.Column(db.Integer, default=0)
    rarity = db.Column(db.String(20), default='common')  # common, rare, epic, legendary

    users = db.relationship('UserBadge', backref='badge', lazy='dynamic')


class UserBadge(db.Model):
    """User badge awards"""
    __tablename__ = 'user_badges'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    badge_id = db.Column(db.String(50), db.ForeignKey('badges.id'), nullable=False)
    awarded_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'badge_id', name='unique_user_badge'),
    )


class Team(db.Model):
    """Team/group for compatibility analysis"""
    __tablename__ = 'teams'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    invite_code = db.Column(db.String(20), unique=True)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    owner = db.relationship('User', foreign_keys=[owner_id])
    members = db.relationship('TeamMember', backref='team', lazy='dynamic', cascade='all, delete-orphan')

    def generate_invite_code(self):
        import random
        import string
        self.invite_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


class TeamMember(db.Model):
    """Team membership"""
    __tablename__ = 'team_members'

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.String(36), db.ForeignKey('teams.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    role = db.Column(db.String(20), default='member')  # owner, admin, member
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('team_id', 'user_id', name='unique_team_member'),
    )


class PersonalityInsight(db.Model):
    """AI-generated insights and recommendations"""
    __tablename__ = 'personality_insights'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    insight_type = db.Column(db.String(50))  # growth, communication, career, relationship
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    based_on = db.Column(db.Text)  # JSON: which results this insight is based on

    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Comparison(db.Model):
    """Saved comparisons between users"""
    __tablename__ = 'comparisons'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user1_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    user2_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    compatibility_score = db.Column(db.Float)
    analysis = db.Column(db.Text)  # JSON: detailed compatibility analysis

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user1 = db.relationship('User', foreign_keys=[user1_id])
    user2 = db.relationship('User', foreign_keys=[user2_id])


def init_badges(db):
    """Initialize default badges"""
    default_badges = [
        # Achievement badges
        Badge(id='first_assessment', name='First Steps', description='Complete your first assessment',
              icon='🎯', category='achievement', xp_reward=50, rarity='common'),
        Badge(id='all_assessments', name='Complete Explorer', description='Complete all assessment types',
              icon='🏆', category='achievement', xp_reward=500, rarity='epic'),
        Badge(id='perfect_consistency', name='True Self', description='Get the same MBTI result 3 times',
              icon='💎', category='achievement', xp_reward=200, rarity='rare'),

        # Streak badges
        Badge(id='streak_7', name='Week Warrior', description='7-day activity streak',
              icon='🔥', category='streak', xp_reward=100, rarity='common'),
        Badge(id='streak_30', name='Monthly Master', description='30-day activity streak',
              icon='⚡', category='streak', xp_reward=300, rarity='rare'),
        Badge(id='streak_100', name='Century Club', description='100-day activity streak',
              icon='👑', category='streak', xp_reward=1000, rarity='legendary'),

        # Social badges
        Badge(id='team_creator', name='Team Builder', description='Create your first team',
              icon='👥', category='social', xp_reward=75, rarity='common'),
        Badge(id='team_5', name='Squad Goals', description='Have 5 members in a team',
              icon='🤝', category='social', xp_reward=150, rarity='rare'),
        Badge(id='share_results', name='Open Book', description='Share your results publicly',
              icon='📢', category='social', xp_reward=50, rarity='common'),

        # Type-specific badges
        Badge(id='analyst', name='Analyst Mind', description='Get an NT type (INTJ, INTP, ENTJ, ENTP)',
              icon='🧠', category='type', xp_reward=25, rarity='common'),
        Badge(id='diplomat', name='Diplomatic Soul', description='Get an NF type (INFJ, INFP, ENFJ, ENFP)',
              icon='💚', category='type', xp_reward=25, rarity='common'),
        Badge(id='sentinel', name='Steadfast Guardian', description='Get an SJ type (ISTJ, ISFJ, ESTJ, ESFJ)',
              icon='🛡️', category='type', xp_reward=25, rarity='common'),
        Badge(id='explorer', name='Bold Explorer', description='Get an SP type (ISTP, ISFP, ESTP, ESFP)',
              icon='🧭', category='type', xp_reward=25, rarity='common'),
    ]

    for badge in default_badges:
        existing = Badge.query.get(badge.id)
        if not existing:
            db.session.add(badge)

    db.session.commit()
