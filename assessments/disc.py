"""
DISC Behavioral Assessment
Measures: Dominance, Influence, Steadiness, Conscientiousness
"""

DISC_QUESTIONS = [
    # Dominance
    {'id': 'd1', 'question': 'I enjoy taking charge of situations.', 'trait': 'D'},
    {'id': 'd2', 'question': 'I am direct and to the point when communicating.', 'trait': 'D'},
    {'id': 'd3', 'question': 'I am comfortable making quick decisions.', 'trait': 'D'},
    {'id': 'd4', 'question': 'I like challenges and competition.', 'trait': 'D'},
    {'id': 'd5', 'question': 'I focus on results over relationships.', 'trait': 'D'},

    # Influence
    {'id': 'i1', 'question': 'I enjoy meeting and talking to new people.', 'trait': 'I'},
    {'id': 'i2', 'question': 'I am optimistic and enthusiastic.', 'trait': 'I'},
    {'id': 'i3', 'question': 'I like to collaborate and work with others.', 'trait': 'I'},
    {'id': 'i4', 'question': 'I express my emotions openly.', 'trait': 'I'},
    {'id': 'i5', 'question': 'I can easily persuade and motivate others.', 'trait': 'I'},

    # Steadiness
    {'id': 's1', 'question': 'I prefer a stable and predictable environment.', 'trait': 'S'},
    {'id': 's2', 'question': 'I am patient and a good listener.', 'trait': 'S'},
    {'id': 's3', 'question': 'I value loyalty and long-term relationships.', 'trait': 'S'},
    {'id': 's4', 'question': 'I prefer to avoid conflict when possible.', 'trait': 'S'},
    {'id': 's5', 'question': 'I like to finish one task before starting another.', 'trait': 'S'},

    # Conscientiousness
    {'id': 'c1', 'question': 'I pay close attention to details and accuracy.', 'trait': 'C'},
    {'id': 'c2', 'question': 'I prefer to follow established rules and procedures.', 'trait': 'C'},
    {'id': 'c3', 'question': 'I think carefully before making decisions.', 'trait': 'C'},
    {'id': 'c4', 'question': 'I value quality over speed.', 'trait': 'C'},
    {'id': 'c5', 'question': 'I like to analyze data before forming conclusions.', 'trait': 'C'},
]

DISC_DESCRIPTIONS = {
    'D': {
        'name': 'Dominance',
        'title': 'The Driver',
        'summary': 'Direct, decisive, and results-oriented. You focus on accomplishing goals and overcoming challenges.',
        'keywords': ['Results', 'Action', 'Challenge', 'Direct', 'Decisive'],
        'strengths': ['Getting results', 'Making decisions', 'Taking charge', 'Problem-solving', 'Self-confidence'],
        'challenges': ['Impatience', 'Insensitivity', 'Poor listening', 'Taking on too much'],
        'communication': 'Be brief, direct, and focus on results. Avoid excessive details.',
        'motivators': ['Power', 'Authority', 'Challenge', 'Competition', 'Results'],
        'stressors': ['Lack of control', 'Routine tasks', 'Slow pace', 'Excessive rules'],
        'color': '#ef4444',
    },
    'I': {
        'name': 'Influence',
        'title': 'The Inspirer',
        'summary': 'Enthusiastic, optimistic, and collaborative. You focus on influencing others and building relationships.',
        'keywords': ['Enthusiasm', 'Collaboration', 'Optimism', 'Recognition', 'Relationships'],
        'strengths': ['Persuading others', 'Building enthusiasm', 'Networking', 'Creativity', 'Team motivation'],
        'challenges': ['Disorganization', 'Lack of follow-through', 'Being overly optimistic', 'Time management'],
        'communication': 'Be friendly, allow time for socializing, and show enthusiasm.',
        'motivators': ['Recognition', 'Approval', 'Popularity', 'Freedom', 'Fun'],
        'stressors': ['Rejection', 'Being ignored', 'Routine work', 'Isolation'],
        'color': '#f97316',
    },
    'S': {
        'name': 'Steadiness',
        'title': 'The Supporter',
        'summary': 'Patient, reliable, and team-oriented. You focus on cooperation and maintaining stability.',
        'keywords': ['Support', 'Stability', 'Patience', 'Loyalty', 'Teamwork'],
        'strengths': ['Listening', 'Team player', 'Reliability', 'Patience', 'Creating harmony'],
        'challenges': ['Resistance to change', 'Difficulty saying no', 'Avoiding conflict', 'Indecisiveness'],
        'communication': 'Be patient, sincere, and allow time for adjustment to change.',
        'motivators': ['Security', 'Stability', 'Appreciation', 'Cooperation', 'Harmony'],
        'stressors': ['Sudden change', 'Conflict', 'Aggression', 'Instability'],
        'color': '#22c55e',
    },
    'C': {
        'name': 'Conscientiousness',
        'title': 'The Analyst',
        'summary': 'Analytical, systematic, and quality-focused. You focus on accuracy and maintaining standards.',
        'keywords': ['Accuracy', 'Analysis', 'Standards', 'Quality', 'Expertise'],
        'strengths': ['Attention to detail', 'Analysis', 'Quality control', 'Planning', 'Problem-solving'],
        'challenges': ['Over-analysis', 'Perfectionism', 'Criticism', 'Slow decision-making'],
        'communication': 'Provide data and logic, be specific, and allow time for analysis.',
        'motivators': ['Quality', 'Accuracy', 'Expertise', 'Logic', 'Standards'],
        'stressors': ['Criticism of work', 'Lack of information', 'Ambiguity', 'Emotional situations'],
        'color': '#3b82f6',
    },
}

# Combined style descriptions for primary/secondary combinations
DISC_COMBINATIONS = {
    'DI': {'name': 'Inspirational', 'description': 'Results-driven with a people focus. Charismatic leaders who drive change through influence.'},
    'DC': {'name': 'Creative', 'description': 'Goal-oriented with attention to quality. Strategic thinkers who achieve through careful planning.'},
    'DS': {'name': 'Driver', 'description': 'Direct but patient. Persistent achievers who stay the course despite obstacles.'},
    'ID': {'name': 'Persuader', 'description': 'Influential and decisive. Motivating leaders who inspire action and results.'},
    'IS': {'name': 'Counselor', 'description': 'Warm and supportive. Empathetic communicators who build lasting relationships.'},
    'IC': {'name': 'Assessor', 'description': 'People-focused with analytical depth. Thoughtful influencers who back enthusiasm with data.'},
    'SD': {'name': 'Achiever', 'description': 'Steady and results-oriented. Reliable performers who consistently deliver.'},
    'SI': {'name': 'Agent', 'description': 'Supportive and friendly. Team players who maintain harmony while driving engagement.'},
    'SC': {'name': 'Technician', 'description': 'Patient and precise. Methodical workers who ensure quality through careful attention.'},
    'CD': {'name': 'Challenger', 'description': 'Analytical and direct. Critical thinkers who question assumptions and drive improvement.'},
    'CI': {'name': 'Appraiser', 'description': 'Detail-oriented yet personable. Diplomatic analysts who present findings with tact.'},
    'CS': {'name': 'Specialist', 'description': 'Precise and patient. Expert practitioners who master their craft through dedication.'},
}


def calculate_disc(answers):
    """
    Calculate DISC profile from Likert scale answers (1-5)
    answers format: {'d1': 4, 'i1': 3, ...}
    """
    scores = {'D': 0, 'I': 0, 'S': 0, 'C': 0}
    counts = {'D': 0, 'I': 0, 'S': 0, 'C': 0}

    question_map = {q['id']: q for q in DISC_QUESTIONS}

    for q_id, answer in answers.items():
        if q_id in question_map:
            q = question_map[q_id]
            trait = q['trait']
            value = int(answer) if isinstance(answer, str) else answer
            scores[trait] += value
            counts[trait] += 1

    # Calculate percentages
    percentages = {}
    for trait in scores:
        if counts[trait] > 0:
            max_score = 5 * counts[trait]
            min_score = 1 * counts[trait]
            normalized = (scores[trait] - min_score) / (max_score - min_score) * 100
            percentages[trait] = round(normalized)
        else:
            percentages[trait] = 50

    # Determine primary and secondary traits
    sorted_traits = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)
    primary = sorted_traits[0]
    secondary = sorted_traits[1]

    # Generate profile type
    result_type = primary + secondary

    return result_type, scores, percentages
