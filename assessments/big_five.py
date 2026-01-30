"""
Big Five (OCEAN) Personality Assessment
Measures: Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism
"""

BIG_FIVE_QUESTIONS = [
    # Openness to Experience
    {'id': 'o1', 'question': 'I have a vivid imagination.', 'trait': 'O', 'reversed': False},
    {'id': 'o2', 'question': 'I am not interested in abstract ideas.', 'trait': 'O', 'reversed': True},
    {'id': 'o3', 'question': 'I enjoy hearing new ideas.', 'trait': 'O', 'reversed': False},
    {'id': 'o4', 'question': 'I tend to vote for conservative political candidates.', 'trait': 'O', 'reversed': True},
    {'id': 'o5', 'question': 'I enjoy artistic and creative experiences.', 'trait': 'O', 'reversed': False},

    # Conscientiousness
    {'id': 'c1', 'question': 'I am always prepared.', 'trait': 'C', 'reversed': False},
    {'id': 'c2', 'question': 'I leave my belongings around.', 'trait': 'C', 'reversed': True},
    {'id': 'c3', 'question': 'I pay attention to details.', 'trait': 'C', 'reversed': False},
    {'id': 'c4', 'question': 'I make a mess of things.', 'trait': 'C', 'reversed': True},
    {'id': 'c5', 'question': 'I get chores done right away.', 'trait': 'C', 'reversed': False},

    # Extraversion
    {'id': 'e1', 'question': 'I am the life of the party.', 'trait': 'E', 'reversed': False},
    {'id': 'e2', 'question': "I don't talk a lot.", 'trait': 'E', 'reversed': True},
    {'id': 'e3', 'question': 'I feel comfortable around people.', 'trait': 'E', 'reversed': False},
    {'id': 'e4', 'question': 'I keep in the background.', 'trait': 'E', 'reversed': True},
    {'id': 'e5', 'question': 'I start conversations.', 'trait': 'E', 'reversed': False},

    # Agreeableness
    {'id': 'a1', 'question': 'I am interested in people.', 'trait': 'A', 'reversed': False},
    {'id': 'a2', 'question': "I insult people.", 'trait': 'A', 'reversed': True},
    {'id': 'a3', 'question': "I sympathize with others' feelings.", 'trait': 'A', 'reversed': False},
    {'id': 'a4', 'question': "I am not interested in other people's problems.", 'trait': 'A', 'reversed': True},
    {'id': 'a5', 'question': 'I have a soft heart.', 'trait': 'A', 'reversed': False},

    # Neuroticism (Emotional Stability reversed)
    {'id': 'n1', 'question': 'I get stressed out easily.', 'trait': 'N', 'reversed': False},
    {'id': 'n2', 'question': 'I am relaxed most of the time.', 'trait': 'N', 'reversed': True},
    {'id': 'n3', 'question': 'I worry about things.', 'trait': 'N', 'reversed': False},
    {'id': 'n4', 'question': 'I seldom feel blue.', 'trait': 'N', 'reversed': True},
    {'id': 'n5', 'question': 'I am easily disturbed.', 'trait': 'N', 'reversed': False},
]

BIG_FIVE_DESCRIPTIONS = {
    'O': {
        'name': 'Openness to Experience',
        'high': {
            'title': 'High Openness',
            'description': 'You are imaginative, creative, and open to new experiences. You appreciate art, emotion, adventure, unusual ideas, and variety.',
            'traits': ['Creative', 'Curious', 'Artistic', 'Imaginative', 'Unconventional'],
        },
        'low': {
            'title': 'Low Openness',
            'description': 'You prefer routine and familiarity. You are practical, conventional, and grounded in reality.',
            'traits': ['Practical', 'Conventional', 'Focused', 'Traditional', 'Down-to-earth'],
        },
        'color': '#8b5cf6',
    },
    'C': {
        'name': 'Conscientiousness',
        'high': {
            'title': 'High Conscientiousness',
            'description': 'You are organized, dependable, and disciplined. You plan ahead, aim for achievement, and control your impulses.',
            'traits': ['Organized', 'Reliable', 'Self-disciplined', 'Hardworking', 'Thorough'],
        },
        'low': {
            'title': 'Low Conscientiousness',
            'description': 'You are flexible and spontaneous. You prefer to go with the flow rather than make detailed plans.',
            'traits': ['Flexible', 'Spontaneous', 'Carefree', 'Easy-going', 'Adaptable'],
        },
        'color': '#10b981',
    },
    'E': {
        'name': 'Extraversion',
        'high': {
            'title': 'High Extraversion',
            'description': 'You are outgoing, energetic, and thrive in social situations. You gain energy from being around others.',
            'traits': ['Outgoing', 'Energetic', 'Talkative', 'Assertive', 'Social'],
        },
        'low': {
            'title': 'Low Extraversion (Introversion)',
            'description': 'You are reserved and prefer solitude or small groups. You gain energy from time alone.',
            'traits': ['Reserved', 'Independent', 'Reflective', 'Quiet', 'Self-contained'],
        },
        'color': '#f43f5e',
    },
    'A': {
        'name': 'Agreeableness',
        'high': {
            'title': 'High Agreeableness',
            'description': 'You are compassionate, cooperative, and value getting along with others. You are trusting and helpful.',
            'traits': ['Cooperative', 'Trusting', 'Helpful', 'Compassionate', 'Kind'],
        },
        'low': {
            'title': 'Low Agreeableness',
            'description': 'You are competitive and skeptical. You prioritize your own interests and question others\' motives.',
            'traits': ['Competitive', 'Skeptical', 'Challenging', 'Detached', 'Analytical'],
        },
        'color': '#06b6d4',
    },
    'N': {
        'name': 'Neuroticism',
        'high': {
            'title': 'High Neuroticism',
            'description': 'You tend to experience negative emotions more intensely. You may be more sensitive to stress and prone to worry.',
            'traits': ['Sensitive', 'Anxious', 'Moody', 'Self-conscious', 'Emotional'],
        },
        'low': {
            'title': 'Low Neuroticism (Emotional Stability)',
            'description': 'You are calm, emotionally stable, and resilient. You handle stress well and rarely feel sad or depressed.',
            'traits': ['Calm', 'Stable', 'Resilient', 'Secure', 'Even-tempered'],
        },
        'color': '#f97316',
    },
}


def calculate_big_five(answers):
    """
    Calculate Big Five scores from Likert scale answers (1-5)
    answers format: {'o1': 4, 'o2': 2, ...}
    """
    scores = {'O': 0, 'C': 0, 'E': 0, 'A': 0, 'N': 0}
    counts = {'O': 0, 'C': 0, 'E': 0, 'A': 0, 'N': 0}

    question_map = {q['id']: q for q in BIG_FIVE_QUESTIONS}

    for q_id, answer in answers.items():
        if q_id in question_map:
            q = question_map[q_id]
            trait = q['trait']

            # Convert answer to numeric (1-5)
            value = int(answer) if isinstance(answer, str) else answer

            # Handle reversed questions
            if q['reversed']:
                value = 6 - value

            scores[trait] += value
            counts[trait] += 1

    # Calculate percentages (normalize to 0-100)
    percentages = {}
    for trait in scores:
        if counts[trait] > 0:
            # Max possible = 5 * count, Min = 1 * count
            max_score = 5 * counts[trait]
            min_score = 1 * counts[trait]
            normalized = (scores[trait] - min_score) / (max_score - min_score) * 100
            percentages[trait] = round(normalized)
        else:
            percentages[trait] = 50

    # Generate profile type
    profile = ''
    for trait in ['O', 'C', 'E', 'A', 'N']:
        if percentages[trait] >= 60:
            profile += trait.upper()
        elif percentages[trait] <= 40:
            profile += trait.lower()
        else:
            profile += '-'

    return profile, scores, percentages
