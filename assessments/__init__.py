"""
AoT (Academy of Tribes) - Assessment Module
Multiple personality assessment frameworks
"""

from .mbti import MBTI_QUESTIONS, MBTI_DESCRIPTIONS, calculate_mbti
from .big_five import BIG_FIVE_QUESTIONS, BIG_FIVE_DESCRIPTIONS, calculate_big_five
from .enneagram import ENNEAGRAM_QUESTIONS, ENNEAGRAM_DESCRIPTIONS, calculate_enneagram
from .disc import DISC_QUESTIONS, DISC_DESCRIPTIONS, calculate_disc
from .cognitive import COGNITIVE_QUESTIONS, COGNITIVE_DESCRIPTIONS, calculate_cognitive_functions

ASSESSMENTS = {
    'mbti': {
        'name': 'MBTI',
        'full_name': 'Myers-Briggs Type Indicator',
        'description': 'Discover your personality type across four dimensions',
        'questions': MBTI_QUESTIONS,
        'descriptions': MBTI_DESCRIPTIONS,
        'calculate': calculate_mbti,
        'question_count': 24,
        'time_estimate': '5-10 min',
        'icon': '🧩',
    },
    'big5': {
        'name': 'Big Five',
        'full_name': 'Big Five Personality Traits (OCEAN)',
        'description': 'Measure your openness, conscientiousness, extraversion, agreeableness, and neuroticism',
        'questions': BIG_FIVE_QUESTIONS,
        'descriptions': BIG_FIVE_DESCRIPTIONS,
        'calculate': calculate_big_five,
        'question_count': 25,
        'time_estimate': '5-8 min',
        'icon': '🌊',
    },
    'enneagram': {
        'name': 'Enneagram',
        'full_name': 'Enneagram of Personality',
        'description': 'Discover your core motivation and growth path among 9 types',
        'questions': ENNEAGRAM_QUESTIONS,
        'descriptions': ENNEAGRAM_DESCRIPTIONS,
        'calculate': calculate_enneagram,
        'question_count': 27,
        'time_estimate': '6-10 min',
        'icon': '⭐',
    },
    'disc': {
        'name': 'DISC',
        'full_name': 'DISC Behavioral Assessment',
        'description': 'Understand your behavioral style in work and relationships',
        'questions': DISC_QUESTIONS,
        'descriptions': DISC_DESCRIPTIONS,
        'calculate': calculate_disc,
        'question_count': 20,
        'time_estimate': '4-6 min',
        'icon': '📊',
    },
    'cognitive': {
        'name': 'Cognitive Functions',
        'full_name': 'Jungian Cognitive Functions',
        'description': 'Deep dive into your cognitive function stack',
        'questions': COGNITIVE_QUESTIONS,
        'descriptions': COGNITIVE_DESCRIPTIONS,
        'calculate': calculate_cognitive_functions,
        'question_count': 32,
        'time_estimate': '8-12 min',
        'icon': '🧠',
    },
}

def get_all_questions(assessment_type):
    """Get flattened list of questions for an assessment"""
    assessment = ASSESSMENTS.get(assessment_type)
    if not assessment:
        return []

    questions = assessment['questions']
    if isinstance(questions, dict):
        all_q = []
        for category, q_list in questions.items():
            all_q.extend(q_list)
        return all_q
    return questions


def get_assessment_info():
    """Get summary info for all assessments"""
    return {
        key: {
            'name': val['name'],
            'full_name': val['full_name'],
            'description': val['description'],
            'question_count': val['question_count'],
            'time_estimate': val['time_estimate'],
            'icon': val['icon'],
        }
        for key, val in ASSESSMENTS.items()
    }
