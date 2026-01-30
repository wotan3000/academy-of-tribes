"""
MBTI (Myers-Briggs Type Indicator) Assessment
"""

MBTI_QUESTIONS = {
    'EI': [
        {'id': 'ei1', 'question': 'At social events, you tend to...', 'option_a': 'Introduce yourself to many new people', 'option_b': 'Stay with people you already know', 'dimension': ('E', 'I')},
        {'id': 'ei2', 'question': 'After a busy week, you prefer to...', 'option_a': 'Go out with friends to recharge', 'option_b': 'Spend quiet time alone to recharge', 'dimension': ('E', 'I')},
        {'id': 'ei3', 'question': 'When working on projects, you prefer...', 'option_a': 'Collaborating with a team', 'option_b': 'Working independently', 'dimension': ('E', 'I')},
        {'id': 'ei4', 'question': 'You get your best ideas when...', 'option_a': 'Discussing with others', 'option_b': 'Reflecting alone', 'dimension': ('E', 'I')},
        {'id': 'ei5', 'question': 'In group discussions, you usually...', 'option_a': 'Speak up readily and often', 'option_b': 'Listen more and speak when you have something important to say', 'dimension': ('E', 'I')},
        {'id': 'ei6', 'question': 'Your ideal weekend involves...', 'option_a': 'Attending events and meeting people', 'option_b': 'Reading, hobbies, or small gatherings', 'dimension': ('E', 'I')},
    ],
    'SN': [
        {'id': 'sn1', 'question': 'When learning something new, you prefer...', 'option_a': 'Step-by-step instructions with concrete examples', 'option_b': 'Understanding the big picture and theory first', 'dimension': ('S', 'N')},
        {'id': 'sn2', 'question': 'You are more interested in...', 'option_a': 'What is real and actual', 'option_b': 'What is possible and potential', 'dimension': ('S', 'N')},
        {'id': 'sn3', 'question': 'When describing an experience, you focus on...', 'option_a': 'Specific details and facts', 'option_b': 'Overall impressions and meanings', 'dimension': ('S', 'N')},
        {'id': 'sn4', 'question': 'You trust more in...', 'option_a': 'Your direct experience and observations', 'option_b': 'Your intuition and hunches', 'dimension': ('S', 'N')},
        {'id': 'sn5', 'question': 'When solving problems, you tend to...', 'option_a': 'Use proven, practical methods', 'option_b': 'Try new, innovative approaches', 'dimension': ('S', 'N')},
        {'id': 'sn6', 'question': 'You find it more interesting to...', 'option_a': 'Maintain and improve existing systems', 'option_b': 'Design and create new systems', 'dimension': ('S', 'N')},
    ],
    'TF': [
        {'id': 'tf1', 'question': 'When making important decisions, you rely more on...', 'option_a': 'Logic and objective analysis', 'option_b': 'Values and how people will be affected', 'dimension': ('T', 'F')},
        {'id': 'tf2', 'question': "When a friend makes a mistake, you're more likely to...", 'option_a': 'Point out what went wrong objectively', 'option_b': 'Consider their feelings first', 'dimension': ('T', 'F')},
        {'id': 'tf3', 'question': 'In disagreements, you prioritize...', 'option_a': 'Finding the truth', 'option_b': 'Maintaining harmony', 'dimension': ('T', 'F')},
        {'id': 'tf4', 'question': 'You are more impressed by...', 'option_a': 'A well-reasoned argument', 'option_b': 'A deeply felt conviction', 'dimension': ('T', 'F')},
        {'id': 'tf5', 'question': 'When giving feedback, you tend to be...', 'option_a': 'Direct and straightforward', 'option_b': 'Tactful and encouraging', 'dimension': ('T', 'F')},
        {'id': 'tf6', 'question': "It's more important for decisions to be...", 'option_a': 'Fair and consistent', 'option_b': 'Compassionate and considerate', 'dimension': ('T', 'F')},
    ],
    'JP': [
        {'id': 'jp1', 'question': 'You prefer your life to be...', 'option_a': 'Planned and organized', 'option_b': 'Flexible and spontaneous', 'dimension': ('J', 'P')},
        {'id': 'jp2', 'question': 'When starting a project, you tend to...', 'option_a': 'Plan thoroughly before beginning', 'option_b': 'Dive in and figure it out as you go', 'dimension': ('J', 'P')},
        {'id': 'jp3', 'question': 'Deadlines make you feel...', 'option_a': 'Comfortable - they help you stay on track', 'option_b': 'Constrained - you work better without them', 'dimension': ('J', 'P')},
        {'id': 'jp4', 'question': 'Your workspace is typically...', 'option_a': 'Neat and organized', 'option_b': 'Cluttered but functional', 'dimension': ('J', 'P')},
        {'id': 'jp5', 'question': 'When making plans with others, you prefer to...', 'option_a': 'Decide details in advance', 'option_b': 'Leave things open-ended', 'dimension': ('J', 'P')},
        {'id': 'jp6', 'question': 'You feel more satisfied when...', 'option_a': 'Tasks are completed and checked off', 'option_b': 'Options remain open', 'dimension': ('J', 'P')},
    ],
}

MBTI_DESCRIPTIONS = {
    'INTJ': {
        'title': 'The Architect',
        'summary': 'Strategic, independent, and determined visionaries who always find a way to achieve their goals.',
        'strengths': ['Strategic thinking', 'Independence', 'Determination', 'High standards', 'Problem-solving'],
        'challenges': ['May seem arrogant', 'Impatient with inefficiency', 'Difficulty with emotions', 'Overly critical'],
        'careers': ['Scientist', 'Engineer', 'Judge', 'Lawyer', 'Project Manager'],
        'famous': ['Elon Musk', 'Friedrich Nietzsche', 'Michelle Obama'],
        'communication': 'Direct and logical. Appreciates efficiency and dislikes small talk.',
        'stress_response': 'Becomes more critical and withdrawn. May overwork or become fixated on problems.',
        'growth_areas': ['Developing emotional intelligence', 'Practicing patience', 'Accepting imperfection'],
        'color': '#6366f1',
    },
    'INTP': {
        'title': 'The Logician',
        'summary': 'Innovative inventors with an unquenchable thirst for knowledge and understanding.',
        'strengths': ['Analytical', 'Objective', 'Imaginative', 'Original', 'Open-minded'],
        'challenges': ['Disconnected', 'Insensitive', 'Condescending', 'Perfectionist'],
        'careers': ['Philosopher', 'Software Developer', 'Scientist', 'Mathematician', 'Technical Writer'],
        'famous': ['Albert Einstein', 'Bill Gates', 'Marie Curie'],
        'communication': 'Precise and theoretical. Enjoys debating ideas for their own sake.',
        'stress_response': 'Becomes more isolated and scattered. May struggle to complete tasks.',
        'growth_areas': ['Following through on projects', 'Connecting with emotions', 'Taking action'],
        'color': '#8b5cf6',
    },
    'ENTJ': {
        'title': 'The Commander',
        'summary': 'Bold, imaginative, and strong-willed leaders who always find a way to succeed.',
        'strengths': ['Efficient', 'Strategic', 'Confident', 'Charismatic', 'Determined'],
        'challenges': ['Stubborn', 'Intolerant', 'Impatient', 'Arrogant'],
        'careers': ['CEO', 'Entrepreneur', 'Lawyer', 'University Professor', 'Business Analyst'],
        'famous': ['Steve Jobs', 'Gordon Ramsay', 'Margaret Thatcher'],
        'communication': 'Assertive and goal-oriented. Focuses on results and efficiency.',
        'stress_response': 'Becomes more controlling and critical. May ignore personal needs.',
        'growth_areas': ['Listening to others', 'Showing vulnerability', 'Patience with process'],
        'color': '#ec4899',
    },
    'ENTP': {
        'title': 'The Debater',
        'summary': 'Smart and curious thinkers who cannot resist an intellectual challenge.',
        'strengths': ['Knowledgeable', 'Quick thinker', 'Original', 'Excellent brainstormer', 'Charismatic'],
        'challenges': ['Argumentative', 'Insensitive', 'Intolerant', 'Unfocused'],
        'careers': ['Entrepreneur', 'Lawyer', 'Consultant', 'Inventor', 'Marketing Director'],
        'famous': ['Thomas Edison', 'Mark Twain', 'Tom Hanks'],
        'communication': 'Energetic and challenging. Loves playing devil\'s advocate.',
        'stress_response': 'Becomes more scattered and argumentative. May make impulsive decisions.',
        'growth_areas': ['Following through', 'Considering feelings', 'Focusing on one thing'],
        'color': '#f43f5e',
    },
    'INFJ': {
        'title': 'The Advocate',
        'summary': 'Quiet and mystical, yet inspiring and tireless idealists.',
        'strengths': ['Insightful', 'Principled', 'Passionate', 'Altruistic', 'Creative'],
        'challenges': ['Sensitive to criticism', 'Perfectionist', 'Burnout prone', 'Private'],
        'careers': ['Counselor', 'Writer', 'Humanitarian', 'Psychologist', 'Teacher'],
        'famous': ['Martin Luther King Jr.', 'Nelson Mandela', 'Mother Teresa'],
        'communication': 'Warm but reserved. Seeks deep, meaningful conversations.',
        'stress_response': 'Becomes withdrawn and may lose perspective. Can become pessimistic.',
        'growth_areas': ['Setting boundaries', 'Self-care', 'Accepting reality'],
        'color': '#10b981',
    },
    'INFP': {
        'title': 'The Mediator',
        'summary': 'Poetic, kind, and altruistic people, always eager to help a good cause.',
        'strengths': ['Empathetic', 'Generous', 'Open-minded', 'Creative', 'Passionate'],
        'challenges': ['Unrealistic', 'Self-isolating', 'Unfocused', 'Emotionally vulnerable'],
        'careers': ['Writer', 'Artist', 'Counselor', 'Social Worker', 'Musician'],
        'famous': ['William Shakespeare', 'J.R.R. Tolkien', 'Princess Diana'],
        'communication': 'Gentle and authentic. Values honesty and emotional depth.',
        'stress_response': 'Becomes more withdrawn and self-critical. May feel misunderstood.',
        'growth_areas': ['Taking action', 'Accepting criticism', 'Being practical'],
        'color': '#14b8a6',
    },
    'ENFJ': {
        'title': 'The Protagonist',
        'summary': 'Charismatic and inspiring leaders, able to mesmerize their listeners.',
        'strengths': ['Receptive', 'Reliable', 'Passionate', 'Altruistic', 'Charismatic'],
        'challenges': ['Overly idealistic', 'Too selfless', 'Sensitive', 'Fluctuating self-esteem'],
        'careers': ['Teacher', 'HR Manager', 'Sales Manager', 'Public Relations', 'Life Coach'],
        'famous': ['Barack Obama', 'Oprah Winfrey', 'Martin Luther King Jr.'],
        'communication': 'Warm and engaging. Naturally attunes to others\' needs.',
        'stress_response': 'Becomes more controlling and self-sacrificing. May neglect own needs.',
        'growth_areas': ['Self-care', 'Accepting imperfection in others', 'Setting limits'],
        'color': '#22c55e',
    },
    'ENFP': {
        'title': 'The Campaigner',
        'summary': 'Enthusiastic, creative, and sociable free spirits who find a reason to smile everywhere.',
        'strengths': ['Curious', 'Observant', 'Energetic', 'Enthusiastic', 'Excellent communicator'],
        'challenges': ['Poor focus', 'Overthinking', 'Easily stressed', 'Approval-seeking'],
        'careers': ['Journalist', 'Actor', 'Consultant', 'Psychologist', 'Entrepreneur'],
        'famous': ['Robin Williams', 'Walt Disney', 'Robert Downey Jr.'],
        'communication': 'Enthusiastic and imaginative. Connects ideas and people easily.',
        'stress_response': 'Becomes scattered and anxious. May seek constant reassurance.',
        'growth_areas': ['Following through', 'Handling routine', 'Managing emotions'],
        'color': '#84cc16',
    },
    'ISTJ': {
        'title': 'The Logistician',
        'summary': 'Practical and fact-minded individuals whose reliability cannot be doubted.',
        'strengths': ['Honest', 'Responsible', 'Calm', 'Practical', 'Order-creating'],
        'challenges': ['Stubborn', 'Insensitive', 'Judgmental', 'Blame-prone'],
        'careers': ['Accountant', 'Military Officer', 'Police Officer', 'Judge', 'Doctor'],
        'famous': ['George Washington', 'Queen Elizabeth II', 'Warren Buffett'],
        'communication': 'Clear and factual. Values precision and reliability.',
        'stress_response': 'Becomes more rigid and pessimistic. May focus on worst-case scenarios.',
        'growth_areas': ['Flexibility', 'Emotional expression', 'Trying new approaches'],
        'color': '#0ea5e9',
    },
    'ISFJ': {
        'title': 'The Defender',
        'summary': 'Very dedicated and warm protectors, always ready to defend their loved ones.',
        'strengths': ['Supportive', 'Reliable', 'Patient', 'Observant', 'Hardworking'],
        'challenges': ['Overworked', 'Shy', 'Repressing feelings', 'Reluctant to change'],
        'careers': ['Nurse', 'Social Worker', 'Counselor', 'Administrator', 'Teacher'],
        'famous': ['Mother Teresa', 'Kate Middleton', 'Rosa Parks'],
        'communication': 'Warm and attentive. Shows care through actions more than words.',
        'stress_response': 'Becomes more anxious about others. May neglect own needs entirely.',
        'growth_areas': ['Asserting needs', 'Accepting change', 'Self-prioritization'],
        'color': '#06b6d4',
    },
    'ESTJ': {
        'title': 'The Executive',
        'summary': 'Excellent administrators, unsurpassed at managing things and people.',
        'strengths': ['Dedicated', 'Strong-willed', 'Direct', 'Honest', 'Organized'],
        'challenges': ['Inflexible', 'Uncomfortable with unconventional', 'Judgmental', 'Workaholic'],
        'careers': ['Business Administrator', 'Manager', 'Police Officer', 'Judge', 'Financial Officer'],
        'famous': ['Sonia Sotomayor', 'John D. Rockefeller', 'Lyndon B. Johnson'],
        'communication': 'Direct and organized. Focuses on tasks and expectations.',
        'stress_response': 'Becomes more controlling and demanding. May be harsh with others.',
        'growth_areas': ['Flexibility', 'Emotional awareness', 'Patience with differences'],
        'color': '#3b82f6',
    },
    'ESFJ': {
        'title': 'The Consul',
        'summary': 'Extraordinarily caring, social, and popular people, always eager to help.',
        'strengths': ['Loyal', 'Sensitive', 'Warm', 'Connecting with others', 'Practical'],
        'challenges': ['Needy', 'Approval-seeking', 'Sensitive to criticism', 'Selfless'],
        'careers': ['Healthcare Worker', 'Teacher', 'Social Worker', 'Sales Representative', 'Counselor'],
        'famous': ['Taylor Swift', 'Bill Clinton', 'Jennifer Garner'],
        'communication': 'Warm and sociable. Remembers details about people.',
        'stress_response': 'Becomes more worried about acceptance. May take things too personally.',
        'growth_areas': ['Independence', 'Accepting criticism', 'Setting boundaries'],
        'color': '#2563eb',
    },
    'ISTP': {
        'title': 'The Virtuoso',
        'summary': 'Bold and practical experimenters, masters of all kinds of tools.',
        'strengths': ['Optimistic', 'Creative', 'Practical', 'Spontaneous', 'Rational'],
        'challenges': ['Insensitive', 'Private', 'Easily bored', 'Risk-prone'],
        'careers': ['Mechanic', 'Engineer', 'Forensic Scientist', 'Pilot', 'Athlete'],
        'famous': ['Clint Eastwood', 'Tom Cruise', 'Bear Grylls'],
        'communication': 'Concise and action-oriented. Prefers showing to telling.',
        'stress_response': 'Becomes more withdrawn or reckless. May take unnecessary risks.',
        'growth_areas': ['Emotional expression', 'Long-term planning', 'Commitment'],
        'color': '#f97316',
    },
    'ISFP': {
        'title': 'The Adventurer',
        'summary': 'Flexible and charming artists, always ready to explore and experience something new.',
        'strengths': ['Charming', 'Sensitive to others', 'Imaginative', 'Passionate', 'Artistic'],
        'challenges': ['Fiercely independent', 'Unpredictable', 'Easily stressed', 'Overly competitive'],
        'careers': ['Artist', 'Musician', 'Designer', 'Photographer', 'Veterinarian'],
        'famous': ['Michael Jackson', 'Marilyn Monroe', 'Bob Dylan'],
        'communication': 'Gentle and expressive. Communicates through art and action.',
        'stress_response': 'Becomes more withdrawn and self-critical. May shut down emotionally.',
        'growth_areas': ['Assertiveness', 'Planning ahead', 'Verbal expression'],
        'color': '#fb923c',
    },
    'ESTP': {
        'title': 'The Entrepreneur',
        'summary': 'Smart, energetic, and very perceptive people who truly enjoy living on the edge.',
        'strengths': ['Bold', 'Rational', 'Practical', 'Original', 'Direct'],
        'challenges': ['Insensitive', 'Impatient', 'Risk-prone', 'Defiant'],
        'careers': ['Entrepreneur', 'Marketing', 'Police Officer', 'Paramedic', 'Sales'],
        'famous': ['Donald Trump', 'Madonna', 'Ernest Hemingway'],
        'communication': 'Direct and energetic. Focuses on immediate action.',
        'stress_response': 'Becomes more impulsive and confrontational. May ignore consequences.',
        'growth_areas': ['Patience', 'Considering long-term', 'Emotional sensitivity'],
        'color': '#ef4444',
    },
    'ESFP': {
        'title': 'The Entertainer',
        'summary': 'Spontaneous, energetic, and enthusiastic people who love to be the center of attention.',
        'strengths': ['Bold', 'Original', 'Practical', 'Observant', 'Excellent people skills'],
        'challenges': ['Sensitive', 'Conflict-averse', 'Easily bored', 'Poor long-term focus'],
        'careers': ['Event Planner', 'Sales', 'Actor', 'Tour Guide', 'Flight Attendant'],
        'famous': ['Marilyn Monroe', 'Jamie Oliver', 'Adam Levine'],
        'communication': 'Fun and engaging. Brings energy to every conversation.',
        'stress_response': 'Becomes more scattered and seeks distraction. May avoid problems.',
        'growth_areas': ['Long-term planning', 'Handling criticism', 'Depth over breadth'],
        'color': '#f87171',
    },
}


def calculate_mbti(answers):
    """Calculate MBTI type from answers"""
    scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

    all_questions = []
    for category, q_list in MBTI_QUESTIONS.items():
        all_questions.extend(q_list)

    question_map = {q['id']: q for q in all_questions}

    for question_id, answer in answers.items():
        if question_id in question_map:
            question = question_map[question_id]
            type_a, type_b = question['dimension']
            if answer == 'A':
                scores[type_a] += 1
            else:
                scores[type_b] += 1

    # Calculate percentages
    e_total = scores['E'] + scores['I']
    s_total = scores['S'] + scores['N']
    t_total = scores['T'] + scores['F']
    j_total = scores['J'] + scores['P']

    percentages = {
        'E': round(scores['E'] / e_total * 100) if e_total > 0 else 50,
        'I': round(scores['I'] / e_total * 100) if e_total > 0 else 50,
        'S': round(scores['S'] / s_total * 100) if s_total > 0 else 50,
        'N': round(scores['N'] / s_total * 100) if s_total > 0 else 50,
        'T': round(scores['T'] / t_total * 100) if t_total > 0 else 50,
        'F': round(scores['F'] / t_total * 100) if t_total > 0 else 50,
        'J': round(scores['J'] / j_total * 100) if j_total > 0 else 50,
        'P': round(scores['P'] / j_total * 100) if j_total > 0 else 50,
    }

    # Determine type
    mbti_type = (
        ('E' if scores['E'] >= scores['I'] else 'I') +
        ('S' if scores['S'] >= scores['N'] else 'N') +
        ('T' if scores['T'] >= scores['F'] else 'F') +
        ('J' if scores['J'] >= scores['P'] else 'P')
    )

    return mbti_type, scores, percentages
