"""
AoT (Academy of Tribes) Platform
Complete Flask Application with User Auth, Multiple Assessments & Advanced Features
"""

import os
import json
from datetime import datetime, timedelta
from functools import wraps

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash

from models import db, User, AssessmentResult, Badge, UserBadge, Team, TeamMember, PersonalityInsight, Comparison, init_badges
from assessments import ASSESSMENTS, get_all_questions, get_assessment_info
from analysis import (
    calculate_mbti_compatibility,
    analyze_team_dynamics,
    generate_growth_recommendations,
    get_communication_guide,
    calculate_personality_coordinates,
    analyze_personality_evolution
)

# ============================================================================
# App Configuration
# ============================================================================

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'aot-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///aot_platform.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Create tables and initialize data
with app.app_context():
    db.create_all()
    init_badges(db)


# ============================================================================
# Utility Functions
# ============================================================================

def award_badge(user, badge_id):
    """Award a badge to a user if they don't already have it"""
    existing = UserBadge.query.filter_by(user_id=user.id, badge_id=badge_id).first()
    if not existing:
        badge = Badge.query.get(badge_id)
        if badge:
            user_badge = UserBadge(user_id=user.id, badge_id=badge_id)
            db.session.add(user_badge)
            user.add_xp(badge.xp_reward)
            db.session.commit()
            return badge
    return None


def check_and_award_badges(user, assessment_type, result_type):
    """Check various badge conditions after assessment completion"""
    awarded = []

    # First assessment badge
    if user.results.count() == 1:
        badge = award_badge(user, 'first_assessment')
        if badge:
            awarded.append(badge)

    # All assessments badge
    completed_types = set(r.assessment_type for r in user.results.all())
    if len(completed_types) == len(ASSESSMENTS):
        badge = award_badge(user, 'all_assessments')
        if badge:
            awarded.append(badge)

    # Type-specific badges for MBTI
    if assessment_type == 'mbti':
        if result_type[1] == 'N' and result_type[2] == 'T':
            award_badge(user, 'analyst')
        elif result_type[1] == 'N' and result_type[2] == 'F':
            award_badge(user, 'diplomat')
        elif result_type[1] == 'S' and result_type[3] == 'J':
            award_badge(user, 'sentinel')
        elif result_type[1] == 'S' and result_type[3] == 'P':
            award_badge(user, 'explorer')

        # Consistency badge - same MBTI 3 times
        mbti_results = user.results.filter_by(assessment_type='mbti').all()
        if len(mbti_results) >= 3:
            last_three = [r.result_type for r in mbti_results[-3:]]
            if len(set(last_three)) == 1:
                badge = award_badge(user, 'perfect_consistency')
                if badge:
                    awarded.append(badge)

    return awarded


# ============================================================================
# Auth Routes
# ============================================================================

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        errors = []
        if not email or '@' not in email:
            errors.append('Valid email is required')
        if not username or len(username) < 3:
            errors.append('Username must be at least 3 characters')
        if len(password) < 8:
            errors.append('Password must be at least 8 characters')
        if password != confirm_password:
            errors.append('Passwords do not match')

        if User.query.filter_by(email=email).first():
            errors.append('Email already registered')
        if User.query.filter_by(username=username).first():
            errors.append('Username already taken')

        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('auth/register.html')

        user = User(email=email, username=username, display_name=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash('Welcome to AoT! Your account has been created.', 'success')
        return redirect(url_for('dashboard'))

    return render_template('auth/register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        remember = request.form.get('remember', False)

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            user.last_login = datetime.utcnow()
            db.session.commit()
            login_user(user, remember=remember)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard'))

        flash('Invalid email or password', 'error')

    return render_template('auth/login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


# ============================================================================
# Main Pages
# ============================================================================

@app.route('/')
def index():
    stats = {
        'total_users': User.query.count(),
        'total_assessments': AssessmentResult.query.count(),
        'assessments': get_assessment_info(),
    }
    return render_template('index.html', stats=stats)


@app.route('/dashboard')
@login_required
def dashboard():
    # Get user's recent results
    recent_results = current_user.results.order_by(
        AssessmentResult.created_at.desc()
    ).limit(5).all()

    # Get primary types
    primary_types = {}
    for assessment_type in ASSESSMENTS:
        result = current_user.results.filter_by(
            assessment_type=assessment_type
        ).order_by(AssessmentResult.created_at.desc()).first()
        if result:
            primary_types[assessment_type] = result.result_type

    # Get badges
    user_badges = UserBadge.query.filter_by(user_id=current_user.id).all()
    badges = [Badge.query.get(ub.badge_id) for ub in user_badges]

    # Get teams
    teams = [tm.team for tm in current_user.teams.all()]

    # Calculate next level XP
    current_xp = current_user.xp_points
    next_level_xp = int(100 * ((current_user.level + 1) ** 1.5))
    current_level_xp = int(100 * (current_user.level ** 1.5))
    xp_progress = ((current_xp - current_level_xp) / (next_level_xp - current_level_xp)) * 100

    return render_template('dashboard.html',
                           recent_results=recent_results,
                           primary_types=primary_types,
                           badges=badges,
                           teams=teams,
                           xp_progress=xp_progress,
                           assessments=get_assessment_info())


# ============================================================================
# Assessment Routes
# ============================================================================

@app.route('/assessments')
def assessments_list():
    """List all available assessments"""
    user_completed = {}
    if current_user.is_authenticated:
        for atype in ASSESSMENTS:
            result = current_user.results.filter_by(assessment_type=atype).first()
            user_completed[atype] = result is not None

    return render_template('assessments/list.html',
                           assessments=get_assessment_info(),
                           user_completed=user_completed)


@app.route('/quiz/<assessment_type>')
def quiz(assessment_type):
    """Take an assessment"""
    if assessment_type not in ASSESSMENTS:
        flash('Assessment not found', 'error')
        return redirect(url_for('assessments_list'))

    assessment = ASSESSMENTS[assessment_type]
    questions = get_all_questions(assessment_type)

    return render_template('assessments/quiz.html',
                           assessment_type=assessment_type,
                           assessment=assessment,
                           questions=questions,
                           total=len(questions))


@app.route('/api/submit/<assessment_type>', methods=['POST'])
def submit_assessment(assessment_type):
    """Submit assessment answers"""
    if assessment_type not in ASSESSMENTS:
        return jsonify({'error': 'Invalid assessment type'}), 400

    data = request.json
    answers = data.get('answers', {})
    time_taken = data.get('time_taken', 0)

    assessment = ASSESSMENTS[assessment_type]
    calculate_func = assessment['calculate']

    # Calculate results
    if assessment_type == 'cognitive':
        result_type, scores, percentages, mbti_match = calculate_func(answers)
        extra_data = {'mbti_match': mbti_match}
    else:
        result_type, scores, percentages = calculate_func(answers)
        extra_data = {}

    # Get description
    descriptions = assessment['descriptions']
    if assessment_type == 'mbti':
        description = descriptions.get(result_type, {})
    elif assessment_type == 'enneagram':
        primary_type = int(result_type[0])
        description = descriptions.get(primary_type, {})
    elif assessment_type == 'disc':
        primary_trait = result_type[0]
        description = descriptions.get(primary_trait, {})
    elif assessment_type == 'big5':
        description = {trait: descriptions[trait] for trait in descriptions}
    elif assessment_type == 'cognitive':
        description = descriptions
    else:
        description = {}

    # Save result
    result = AssessmentResult(
        user_id=current_user.id if current_user.is_authenticated else None,
        assessment_type=assessment_type,
        result_type=result_type,
        time_taken=time_taken,
    )
    result.set_scores(scores)
    result.set_percentages(percentages)

    db.session.add(result)
    db.session.commit()

    # Award badges and XP if logged in
    badges_awarded = []
    if current_user.is_authenticated:
        current_user.add_xp(25)  # Base XP for completing an assessment
        badges_awarded = check_and_award_badges(current_user, assessment_type, result_type)
        db.session.commit()

    response = {
        'result_id': result.id,
        'type': result_type,
        'scores': scores,
        'percentages': percentages,
        'description': description,
        'badges_awarded': [{'name': b.name, 'icon': b.icon} for b in badges_awarded],
        **extra_data,
    }

    return jsonify(response)


@app.route('/results/<result_id>')
def view_result(result_id):
    """View assessment result"""
    result = AssessmentResult.query.get_or_404(result_id)

    assessment = ASSESSMENTS.get(result.assessment_type, {})
    descriptions = assessment.get('descriptions', {})

    # Get appropriate description
    if result.assessment_type == 'mbti':
        description = descriptions.get(result.result_type, {})
    elif result.assessment_type == 'enneagram':
        primary_type = int(result.result_type[0])
        description = descriptions.get(primary_type, {})
    elif result.assessment_type == 'disc':
        primary_trait = result.result_type[0]
        description = descriptions.get(primary_trait, {})
    else:
        description = descriptions

    return render_template('assessments/result.html',
                           result=result,
                           assessment=assessment,
                           description=description,
                           percentages=result.get_percentages())


# ============================================================================
# Analysis & Insights Routes
# ============================================================================

@app.route('/compatibility')
@login_required
def compatibility():
    """Compatibility analysis page"""
    # Get user's MBTI type
    mbti_result = current_user.results.filter_by(
        assessment_type='mbti'
    ).order_by(AssessmentResult.created_at.desc()).first()

    user_type = mbti_result.result_type if mbti_result else None

    return render_template('analysis/compatibility.html',
                           user_type=user_type,
                           all_types=list(ASSESSMENTS['mbti']['descriptions'].keys()))


@app.route('/api/compatibility', methods=['POST'])
def api_compatibility():
    """Calculate compatibility between two types"""
    data = request.json
    type1 = data.get('type1', '').upper()
    type2 = data.get('type2', '').upper()

    if not type1 or not type2:
        return jsonify({'error': 'Both types are required'}), 400

    result = calculate_mbti_compatibility(type1, type2)
    communication = get_communication_guide(type1, type2)

    return jsonify({
        'compatibility': result,
        'communication': communication,
    })


@app.route('/insights')
@login_required
def insights():
    """Personal insights page"""
    # Get all user's results
    all_results = current_user.results.order_by(AssessmentResult.created_at.asc()).all()

    # Analyze evolution
    mbti_results = [r.to_dict() for r in all_results if r.assessment_type == 'mbti']
    evolution = analyze_personality_evolution(mbti_results) if mbti_results else None

    # Get growth recommendations
    mbti_type = current_user.get_primary_type('mbti')
    growth = generate_growth_recommendations(mbti_type) if mbti_type else None

    # Get enneagram type for additional insights
    enneagram_type = current_user.get_primary_type('enneagram')

    return render_template('analysis/insights.html',
                           evolution=evolution,
                           growth=growth,
                           mbti_type=mbti_type,
                           enneagram_type=enneagram_type)


# ============================================================================
# Team Routes
# ============================================================================

@app.route('/teams')
@login_required
def teams_list():
    """List user's teams"""
    user_teams = [tm.team for tm in current_user.teams.all()]
    return render_template('teams/list.html', teams=user_teams)


@app.route('/teams/create', methods=['GET', 'POST'])
@login_required
def create_team():
    """Create a new team"""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()

        if not name:
            flash('Team name is required', 'error')
            return render_template('teams/create.html')

        team = Team(name=name, description=description, owner_id=current_user.id)
        team.generate_invite_code()
        db.session.add(team)

        # Add creator as owner member
        membership = TeamMember(team=team, user_id=current_user.id, role='owner')
        db.session.add(membership)

        db.session.commit()

        # Award badge
        award_badge(current_user, 'team_creator')

        flash(f'Team "{name}" created! Invite code: {team.invite_code}', 'success')
        return redirect(url_for('view_team', team_id=team.id))

    return render_template('teams/create.html')


@app.route('/teams/<team_id>')
@login_required
def view_team(team_id):
    """View team details and analysis"""
    team = Team.query.get_or_404(team_id)

    # Check if user is a member
    membership = TeamMember.query.filter_by(team_id=team_id, user_id=current_user.id).first()
    if not membership and not team.is_public:
        flash('You are not a member of this team', 'error')
        return redirect(url_for('teams_list'))

    # Get all members and their types
    members = []
    team_types = []
    for tm in team.members.all():
        user = tm.user
        mbti_type = user.get_primary_type('mbti')
        members.append({
            'user': user,
            'role': tm.role,
            'mbti_type': mbti_type,
        })
        if mbti_type:
            team_types.append(mbti_type)

    # Analyze team dynamics
    dynamics = analyze_team_dynamics(team_types) if team_types else None

    return render_template('teams/view.html',
                           team=team,
                           members=members,
                           dynamics=dynamics,
                           is_owner=team.owner_id == current_user.id)


@app.route('/teams/join', methods=['POST'])
@login_required
def join_team():
    """Join a team with invite code"""
    invite_code = request.form.get('invite_code', '').strip().upper()

    team = Team.query.filter_by(invite_code=invite_code).first()
    if not team:
        flash('Invalid invite code', 'error')
        return redirect(url_for('teams_list'))

    # Check if already a member
    existing = TeamMember.query.filter_by(team_id=team.id, user_id=current_user.id).first()
    if existing:
        flash('You are already a member of this team', 'info')
        return redirect(url_for('view_team', team_id=team.id))

    membership = TeamMember(team_id=team.id, user_id=current_user.id, role='member')
    db.session.add(membership)
    db.session.commit()

    # Check for team size badge
    if team.members.count() >= 5:
        for tm in team.members.all():
            award_badge(tm.user, 'team_5')

    flash(f'You have joined "{team.name}"!', 'success')
    return redirect(url_for('view_team', team_id=team.id))


# ============================================================================
# Profile Routes
# ============================================================================

@app.route('/profile')
@login_required
def profile():
    """User profile page"""
    return render_template('profile/view.html', user=current_user)


@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """Edit user profile"""
    if request.method == 'POST':
        current_user.display_name = request.form.get('display_name', current_user.username)
        current_user.bio = request.form.get('bio', '')
        current_user.is_public = request.form.get('is_public') == 'on'
        current_user.theme = request.form.get('theme', 'dark')

        db.session.commit()
        flash('Profile updated!', 'success')
        return redirect(url_for('profile'))

    return render_template('profile/edit.html', user=current_user)


@app.route('/profile/<username>')
def public_profile(username):
    """View public profile"""
    user = User.query.filter_by(username=username).first_or_404()

    if not user.is_public and (not current_user.is_authenticated or current_user.id != user.id):
        flash('This profile is private', 'info')
        return redirect(url_for('index'))

    # Get public results
    results = {}
    if user.show_results:
        for atype in ASSESSMENTS:
            result = user.results.filter_by(assessment_type=atype).order_by(
                AssessmentResult.created_at.desc()
            ).first()
            if result:
                results[atype] = result.result_type

    return render_template('profile/public.html', user=user, results=results)


# ============================================================================
# Static Pages
# ============================================================================

@app.route('/types')
def all_types():
    """View all personality types"""
    return render_template('types.html', types=ASSESSMENTS['mbti']['descriptions'])


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


# ============================================================================
# API Endpoints
# ============================================================================

@app.route('/api/stats')
def api_stats():
    """Get platform statistics"""
    type_counts = db.session.query(
        AssessmentResult.result_type,
        db.func.count(AssessmentResult.id)
    ).filter(
        AssessmentResult.assessment_type == 'mbti'
    ).group_by(AssessmentResult.result_type).all()

    return jsonify({
        'total_users': User.query.count(),
        'total_assessments': AssessmentResult.query.count(),
        'type_distribution': {t: c for t, c in type_counts},
    })


@app.route('/api/results/<result_id>')
def api_result(result_id):
    """Get result data via API"""
    result = AssessmentResult.query.get_or_404(result_id)

    assessment = ASSESSMENTS.get(result.assessment_type, {})
    descriptions = assessment.get('descriptions', {})

    if result.assessment_type == 'mbti':
        description = descriptions.get(result.result_type, {})
    elif result.assessment_type == 'enneagram':
        primary_type = int(result.result_type[0])
        description = descriptions.get(primary_type, {})
    elif result.assessment_type == 'disc':
        primary_trait = result.result_type[0]
        description = descriptions.get(primary_trait, {})
    else:
        description = descriptions

    return jsonify({
        'type': result.result_type,
        'percentages': result.get_percentages(),
        'description': description,
        'assessment_type': result.assessment_type,
        'created_at': result.created_at.isoformat() if result.created_at else None,
    })


# ============================================================================
# Error Handlers
# ============================================================================

@app.errorhandler(404)
def not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('errors/500.html'), 500


# ============================================================================
# Run Application
# ============================================================================

if __name__ == '__main__':
    app.run(debug=True, port=5000)
