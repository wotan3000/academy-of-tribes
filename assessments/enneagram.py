"""
Enneagram of Personality Assessment
9 Core Types with Wings and Growth/Stress Paths
"""

ENNEAGRAM_QUESTIONS = [
    # Type 1 - The Reformer
    {'id': 'e1_1', 'question': 'I have a strong sense of right and wrong.', 'type': 1},
    {'id': 'e1_2', 'question': 'I notice mistakes and imperfections easily.', 'type': 1},
    {'id': 'e1_3', 'question': 'I strive to improve myself and my environment.', 'type': 1},

    # Type 2 - The Helper
    {'id': 'e2_1', 'question': 'I naturally sense what others need.', 'type': 2},
    {'id': 'e2_2', 'question': 'I feel good about myself when I help others.', 'type': 2},
    {'id': 'e2_3', 'question': 'I often put others\' needs before my own.', 'type': 2},

    # Type 3 - The Achiever
    {'id': 'e3_1', 'question': 'Success and achievement are very important to me.', 'type': 3},
    {'id': 'e3_2', 'question': 'I adapt my presentation to impress others.', 'type': 3},
    {'id': 'e3_3', 'question': 'I am highly driven and goal-oriented.', 'type': 3},

    # Type 4 - The Individualist
    {'id': 'e4_1', 'question': 'I often feel different from others.', 'type': 4},
    {'id': 'e4_2', 'question': 'I have deep, intense emotions.', 'type': 4},
    {'id': 'e4_3', 'question': 'Authenticity and self-expression are crucial to me.', 'type': 4},

    # Type 5 - The Investigator
    {'id': 'e5_1', 'question': 'I need time alone to recharge and think.', 'type': 5},
    {'id': 'e5_2', 'question': 'I prefer to observe before participating.', 'type': 5},
    {'id': 'e5_3', 'question': 'Knowledge and understanding drive me.', 'type': 5},

    # Type 6 - The Loyalist
    {'id': 'e6_1', 'question': 'I often anticipate potential problems.', 'type': 6},
    {'id': 'e6_2', 'question': 'Loyalty and reliability are core values for me.', 'type': 6},
    {'id': 'e6_3', 'question': 'I seek security and guidance from trusted sources.', 'type': 6},

    # Type 7 - The Enthusiast
    {'id': 'e7_1', 'question': 'I love having many options and possibilities.', 'type': 7},
    {'id': 'e7_2', 'question': 'I quickly move from one interest to another.', 'type': 7},
    {'id': 'e7_3', 'question': 'I avoid pain and seek pleasurable experiences.', 'type': 7},

    # Type 8 - The Challenger
    {'id': 'e8_1', 'question': 'I am direct and assertive in expressing my views.', 'type': 8},
    {'id': 'e8_2', 'question': 'I protect those who cannot protect themselves.', 'type': 8},
    {'id': 'e8_3', 'question': 'I dislike feeling controlled or vulnerable.', 'type': 8},

    # Type 9 - The Peacemaker
    {'id': 'e9_1', 'question': 'I go along with others to keep the peace.', 'type': 9},
    {'id': 'e9_2', 'question': 'I can see multiple perspectives easily.', 'type': 9},
    {'id': 'e9_3', 'question': 'I sometimes struggle to know what I want.', 'type': 9},
]

ENNEAGRAM_DESCRIPTIONS = {
    1: {
        'title': 'The Reformer',
        'core_motivation': 'To be good, right, and perfect',
        'core_fear': 'Being corrupt, evil, or defective',
        'summary': 'Principled, purposeful, self-controlled, and perfectionistic.',
        'strengths': ['Ethical', 'Reliable', 'Productive', 'Wise', 'Idealistic'],
        'challenges': ['Critical', 'Inflexible', 'Self-righteous', 'Impatient'],
        'growth_path': 'Move toward Type 7 (spontaneity and joy)',
        'stress_path': 'Move toward Type 4 (moodiness and self-pity)',
        'wings': ['1w9 (The Idealist)', '1w2 (The Advocate)'],
        'famous': ['Mahatma Gandhi', 'Nelson Mandela', 'Martha Stewart'],
        'color': '#6366f1',
    },
    2: {
        'title': 'The Helper',
        'core_motivation': 'To be loved and needed',
        'core_fear': 'Being unwanted or unloved',
        'summary': 'Generous, demonstrative, people-pleasing, and possessive.',
        'strengths': ['Caring', 'Interpersonal', 'Generous', 'Warm', 'Supportive'],
        'challenges': ['People-pleasing', 'Possessive', 'Intrusive', 'Martyr-like'],
        'growth_path': 'Move toward Type 4 (self-awareness and authenticity)',
        'stress_path': 'Move toward Type 8 (aggressive and controlling)',
        'wings': ['2w1 (The Servant)', '2w3 (The Host/Hostess)'],
        'famous': ['Mother Teresa', 'Desmond Tutu', 'Eleanor Roosevelt'],
        'color': '#ec4899',
    },
    3: {
        'title': 'The Achiever',
        'core_motivation': 'To be valuable and worthwhile',
        'core_fear': 'Being worthless or without value',
        'summary': 'Adaptable, excelling, driven, and image-conscious.',
        'strengths': ['Optimistic', 'Confident', 'Industrious', 'Efficient', 'Charming'],
        'challenges': ['Competitive', 'Workaholic', 'Image-focused', 'Deceptive'],
        'growth_path': 'Move toward Type 6 (commitment and cooperation)',
        'stress_path': 'Move toward Type 9 (disengaged and apathetic)',
        'wings': ['3w2 (The Charmer)', '3w4 (The Professional)'],
        'famous': ['Oprah Winfrey', 'Tony Robbins', 'Tom Cruise'],
        'color': '#f43f5e',
    },
    4: {
        'title': 'The Individualist',
        'core_motivation': 'To find their identity and significance',
        'core_fear': 'Having no identity or personal significance',
        'summary': 'Expressive, dramatic, self-absorbed, and temperamental.',
        'strengths': ['Creative', 'Intuitive', 'Honest', 'Compassionate', 'Unique'],
        'challenges': ['Moody', 'Self-absorbed', 'Envious', 'Withdrawn'],
        'growth_path': 'Move toward Type 1 (principled and objective)',
        'stress_path': 'Move toward Type 2 (clingy and needy)',
        'wings': ['4w3 (The Aristocrat)', '4w5 (The Bohemian)'],
        'famous': ['Prince', 'Frida Kahlo', 'Johnny Depp'],
        'color': '#8b5cf6',
    },
    5: {
        'title': 'The Investigator',
        'core_motivation': 'To be capable and competent',
        'core_fear': 'Being useless or incompetent',
        'summary': 'Perceptive, innovative, secretive, and isolated.',
        'strengths': ['Analytical', 'Objective', 'Perceptive', 'Self-sufficient', 'Inventive'],
        'challenges': ['Detached', 'Isolated', 'Stingy', 'Provocative'],
        'growth_path': 'Move toward Type 8 (self-confident and decisive)',
        'stress_path': 'Move toward Type 7 (scattered and impulsive)',
        'wings': ['5w4 (The Iconoclast)', '5w6 (The Problem Solver)'],
        'famous': ['Albert Einstein', 'Stephen Hawking', 'Bill Gates'],
        'color': '#14b8a6',
    },
    6: {
        'title': 'The Loyalist',
        'core_motivation': 'To have security and support',
        'core_fear': 'Being without support or guidance',
        'summary': 'Engaging, responsible, anxious, and suspicious.',
        'strengths': ['Loyal', 'Responsible', 'Hardworking', 'Trustworthy', 'Practical'],
        'challenges': ['Anxious', 'Suspicious', 'Reactive', 'Defensive'],
        'growth_path': 'Move toward Type 9 (relaxed and optimistic)',
        'stress_path': 'Move toward Type 3 (competitive and arrogant)',
        'wings': ['6w5 (The Defender)', '6w7 (The Buddy)'],
        'famous': ['Jennifer Aniston', 'Tom Hanks', 'Princess Diana'],
        'color': '#0ea5e9',
    },
    7: {
        'title': 'The Enthusiast',
        'core_motivation': 'To be satisfied and content',
        'core_fear': 'Being deprived or in pain',
        'summary': 'Spontaneous, versatile, acquisitive, and scattered.',
        'strengths': ['Optimistic', 'Versatile', 'Spontaneous', 'Playful', 'Practical'],
        'challenges': ['Scattered', 'Uncommitted', 'Impatient', 'Escapist'],
        'growth_path': 'Move toward Type 5 (focused and profound)',
        'stress_path': 'Move toward Type 1 (critical and perfectionist)',
        'wings': ['7w6 (The Entertainer)', '7w8 (The Realist)'],
        'famous': ['Robin Williams', 'Jim Carrey', 'Richard Branson'],
        'color': '#f97316',
    },
    8: {
        'title': 'The Challenger',
        'core_motivation': 'To protect themselves and control their destiny',
        'core_fear': 'Being harmed or controlled by others',
        'summary': 'Self-confident, decisive, willful, and confrontational.',
        'strengths': ['Powerful', 'Confident', 'Protective', 'Direct', 'Resourceful'],
        'challenges': ['Domineering', 'Confrontational', 'Insensitive', 'Intimidating'],
        'growth_path': 'Move toward Type 2 (caring and open-hearted)',
        'stress_path': 'Move toward Type 5 (withdrawn and secretive)',
        'wings': ['8w7 (The Maverick)', '8w9 (The Bear)'],
        'famous': ['Martin Luther King Jr.', 'Winston Churchill', 'Kamala Harris'],
        'color': '#ef4444',
    },
    9: {
        'title': 'The Peacemaker',
        'core_motivation': 'To have inner peace and harmony',
        'core_fear': 'Loss and separation',
        'summary': 'Receptive, reassuring, complacent, and resigned.',
        'strengths': ['Peaceful', 'Easygoing', 'Accepting', 'Supportive', 'Patient'],
        'challenges': ['Passive', 'Complacent', 'Stubborn', 'Indecisive'],
        'growth_path': 'Move toward Type 3 (self-developing and energetic)',
        'stress_path': 'Move toward Type 6 (anxious and worried)',
        'wings': ['9w8 (The Referee)', '9w1 (The Dreamer)'],
        'famous': ['Barack Obama', 'Queen Elizabeth II', 'Morgan Freeman'],
        'color': '#22c55e',
    },
}


def calculate_enneagram(answers):
    """
    Calculate Enneagram type from Likert scale answers (1-5)
    answers format: {'e1_1': 4, 'e2_1': 2, ...}
    """
    type_scores = {i: 0 for i in range(1, 10)}
    type_counts = {i: 0 for i in range(1, 10)}

    question_map = {q['id']: q for q in ENNEAGRAM_QUESTIONS}

    for q_id, answer in answers.items():
        if q_id in question_map:
            q = question_map[q_id]
            etype = q['type']
            value = int(answer) if isinstance(answer, str) else answer
            type_scores[etype] += value
            type_counts[etype] += 1

    # Calculate percentages for each type
    percentages = {}
    for etype in range(1, 10):
        if type_counts[etype] > 0:
            max_score = 5 * type_counts[etype]
            min_score = 1 * type_counts[etype]
            normalized = (type_scores[etype] - min_score) / (max_score - min_score) * 100
            percentages[etype] = round(normalized)
        else:
            percentages[etype] = 0

    # Find primary type
    primary_type = max(type_scores, key=type_scores.get)

    # Determine wing (adjacent type with higher score)
    wing_options = [(primary_type - 1) if primary_type > 1 else 9,
                    (primary_type + 1) if primary_type < 9 else 1]
    wing = max(wing_options, key=lambda x: type_scores[x])

    result_type = f"{primary_type}w{wing}"

    return result_type, type_scores, percentages
