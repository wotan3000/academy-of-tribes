"""
Jungian Cognitive Functions Assessment
Measures the 8 cognitive functions: Se, Si, Ne, Ni, Te, Ti, Fe, Fi
"""

COGNITIVE_QUESTIONS = [
    # Extraverted Sensing (Se)
    {'id': 'se1', 'question': 'I notice physical details in my environment that others miss.', 'function': 'Se'},
    {'id': 'se2', 'question': 'I enjoy thrilling, in-the-moment experiences.', 'function': 'Se'},
    {'id': 'se3', 'question': 'I am highly aware of sensory experiences (taste, touch, sight, sound).', 'function': 'Se'},
    {'id': 'se4', 'question': 'I prefer to act in the moment rather than plan ahead.', 'function': 'Se'},

    # Introverted Sensing (Si)
    {'id': 'si1', 'question': 'I often compare current experiences to past ones.', 'function': 'Si'},
    {'id': 'si2', 'question': 'I have a good memory for details and facts.', 'function': 'Si'},
    {'id': 'si3', 'question': 'I value traditions and established methods.', 'function': 'Si'},
    {'id': 'si4', 'question': 'I am comforted by familiar routines and environments.', 'function': 'Si'},

    # Extraverted Intuition (Ne)
    {'id': 'ne1', 'question': 'I easily see multiple possibilities in any situation.', 'function': 'Ne'},
    {'id': 'ne2', 'question': 'I make unexpected connections between unrelated ideas.', 'function': 'Ne'},
    {'id': 'ne3', 'question': 'I get excited about brainstorming and exploring new concepts.', 'function': 'Ne'},
    {'id': 'ne4', 'question': 'I often wonder "what if" about future possibilities.', 'function': 'Ne'},

    # Introverted Intuition (Ni)
    {'id': 'ni1', 'question': 'I often have sudden insights or "aha" moments.', 'function': 'Ni'},
    {'id': 'ni2', 'question': 'I can sense how things will unfold in the future.', 'function': 'Ni'},
    {'id': 'ni3', 'question': 'I focus intensely on a single vision or goal.', 'function': 'Ni'},
    {'id': 'ni4', 'question': 'I understand complex patterns that others don\'t see.', 'function': 'Ni'},

    # Extraverted Thinking (Te)
    {'id': 'te1', 'question': 'I naturally organize people and resources to achieve goals.', 'function': 'Te'},
    {'id': 'te2', 'question': 'I value efficiency and getting things done.', 'function': 'Te'},
    {'id': 'te3', 'question': 'I prefer objective data over personal opinions when deciding.', 'function': 'Te'},
    {'id': 'te4', 'question': 'I think out loud and express my reasoning directly.', 'function': 'Te'},

    # Introverted Thinking (Ti)
    {'id': 'ti1', 'question': 'I need to understand how things work at a fundamental level.', 'function': 'Ti'},
    {'id': 'ti2', 'question': 'I create my own mental frameworks to understand the world.', 'function': 'Ti'},
    {'id': 'ti3', 'question': 'I value logical consistency above all else.', 'function': 'Ti'},
    {'id': 'ti4', 'question': 'I often question widely accepted truths.', 'function': 'Ti'},

    # Extraverted Feeling (Fe)
    {'id': 'fe1', 'question': 'I easily sense the emotional atmosphere of a group.', 'function': 'Fe'},
    {'id': 'fe2', 'question': 'I naturally work to create harmony among people.', 'function': 'Fe'},
    {'id': 'fe3', 'question': 'I express my emotions openly and easily.', 'function': 'Fe'},
    {'id': 'fe4', 'question': 'I adapt my behavior to make others comfortable.', 'function': 'Fe'},

    # Introverted Feeling (Fi)
    {'id': 'fi1', 'question': 'I have a strong inner sense of what is right and wrong.', 'function': 'Fi'},
    {'id': 'fi2', 'question': 'I need my actions to align with my personal values.', 'function': 'Fi'},
    {'id': 'fi3', 'question': 'I feel emotions deeply but may not express them outwardly.', 'function': 'Fi'},
    {'id': 'fi4', 'question': 'Authenticity is more important to me than fitting in.', 'function': 'Fi'},
]

COGNITIVE_DESCRIPTIONS = {
    'Se': {
        'name': 'Extraverted Sensing',
        'title': 'The Experiencer',
        'summary': 'Focused on the immediate physical environment and sensory experiences.',
        'strengths': ['Present awareness', 'Quick reflexes', 'Aesthetic appreciation', 'Practical action'],
        'when_dominant': 'You live fully in the moment, taking in sensory details and responding quickly to your environment.',
        'when_auxiliary': 'You balance your primary function with keen awareness of your surroundings.',
        'when_inferior': 'Under stress, you may overindulge in sensory experiences or become reckless.',
        'color': '#ef4444',
    },
    'Si': {
        'name': 'Introverted Sensing',
        'title': 'The Preserver',
        'summary': 'Focused on internal sensations and detailed memories of past experiences.',
        'strengths': ['Detailed memory', 'Reliability', 'Tradition', 'Practical knowledge'],
        'when_dominant': 'You have rich, detailed memories and value traditions and proven methods.',
        'when_auxiliary': 'You draw on past experience to support your primary way of processing.',
        'when_inferior': 'Under stress, you may become obsessed with physical symptoms or nostalgic.',
        'color': '#f97316',
    },
    'Ne': {
        'name': 'Extraverted Intuition',
        'title': 'The Explorer',
        'summary': 'Focused on patterns, possibilities, and connections in the external world.',
        'strengths': ['Innovation', 'Brainstorming', 'Adaptability', 'Seeing possibilities'],
        'when_dominant': 'You see endless possibilities and make unexpected connections between ideas.',
        'when_auxiliary': 'You use possibilities to enhance and expand your primary function.',
        'when_inferior': 'Under stress, you may become paranoid about worst-case scenarios.',
        'color': '#84cc16',
    },
    'Ni': {
        'name': 'Introverted Intuition',
        'title': 'The Visionary',
        'summary': 'Focused on internal insights, patterns, and future implications.',
        'strengths': ['Long-term vision', 'Pattern recognition', 'Strategic thinking', 'Insight'],
        'when_dominant': 'You have powerful insights and a clear sense of how things will unfold.',
        'when_auxiliary': 'Your insights inform and deepen your primary way of engaging.',
        'when_inferior': 'Under stress, you may become obsessed with dark visions of the future.',
        'color': '#8b5cf6',
    },
    'Te': {
        'name': 'Extraverted Thinking',
        'title': 'The Director',
        'summary': 'Focused on organizing the external world efficiently and logically.',
        'strengths': ['Organization', 'Efficiency', 'Decision-making', 'Goal achievement'],
        'when_dominant': 'You naturally organize systems and people to achieve measurable results.',
        'when_auxiliary': 'You use logical structure to support your primary function effectively.',
        'when_inferior': 'Under stress, you may become harshly critical or obsessed with control.',
        'color': '#3b82f6',
    },
    'Ti': {
        'name': 'Introverted Thinking',
        'title': 'The Analyst',
        'summary': 'Focused on building internal logical frameworks and understanding.',
        'strengths': ['Analysis', 'Problem-solving', 'Logical consistency', 'Independence'],
        'when_dominant': 'You build comprehensive internal models to understand how things work.',
        'when_auxiliary': 'Your logical analysis supports and refines your primary function.',
        'when_inferior': 'Under stress, you may become obsessed with finding logical inconsistencies.',
        'color': '#06b6d4',
    },
    'Fe': {
        'name': 'Extraverted Feeling',
        'title': 'The Harmonizer',
        'summary': 'Focused on harmony, social dynamics, and others\' emotional needs.',
        'strengths': ['Empathy', 'Social awareness', 'Harmony building', 'Communication'],
        'when_dominant': 'You naturally attune to others\' feelings and work to create group harmony.',
        'when_auxiliary': 'You use social awareness to enhance your primary function\'s effectiveness.',
        'when_inferior': 'Under stress, you may become overly concerned with others\' approval.',
        'color': '#ec4899',
    },
    'Fi': {
        'name': 'Introverted Feeling',
        'title': 'The Idealist',
        'summary': 'Focused on internal values, authenticity, and personal meaning.',
        'strengths': ['Authenticity', 'Values clarity', 'Empathy', 'Individuality'],
        'when_dominant': 'You have a strong inner compass of values guiding all your decisions.',
        'when_auxiliary': 'Your values provide depth and meaning to your primary function.',
        'when_inferior': 'Under stress, you may become hypersensitive or withdraw emotionally.',
        'color': '#14b8a6',
    },
}

# Function stacks for each MBTI type
MBTI_FUNCTION_STACKS = {
    'INTJ': ['Ni', 'Te', 'Fi', 'Se'],
    'INTP': ['Ti', 'Ne', 'Si', 'Fe'],
    'ENTJ': ['Te', 'Ni', 'Se', 'Fi'],
    'ENTP': ['Ne', 'Ti', 'Fe', 'Si'],
    'INFJ': ['Ni', 'Fe', 'Ti', 'Se'],
    'INFP': ['Fi', 'Ne', 'Si', 'Te'],
    'ENFJ': ['Fe', 'Ni', 'Se', 'Ti'],
    'ENFP': ['Ne', 'Fi', 'Te', 'Si'],
    'ISTJ': ['Si', 'Te', 'Fi', 'Ne'],
    'ISFJ': ['Si', 'Fe', 'Ti', 'Ne'],
    'ESTJ': ['Te', 'Si', 'Ne', 'Fi'],
    'ESFJ': ['Fe', 'Si', 'Ne', 'Ti'],
    'ISTP': ['Ti', 'Se', 'Ni', 'Fe'],
    'ISFP': ['Fi', 'Se', 'Ni', 'Te'],
    'ESTP': ['Se', 'Ti', 'Fe', 'Ni'],
    'ESFP': ['Se', 'Fi', 'Te', 'Ni'],
}


def calculate_cognitive_functions(answers):
    """
    Calculate cognitive function scores from Likert scale answers (1-5)
    answers format: {'se1': 4, 'ni1': 5, ...}
    """
    scores = {func: 0 for func in ['Se', 'Si', 'Ne', 'Ni', 'Te', 'Ti', 'Fe', 'Fi']}
    counts = {func: 0 for func in scores}

    question_map = {q['id']: q for q in COGNITIVE_QUESTIONS}

    for q_id, answer in answers.items():
        if q_id in question_map:
            q = question_map[q_id]
            func = q['function']
            value = int(answer) if isinstance(answer, str) else answer
            scores[func] += value
            counts[func] += 1

    # Calculate percentages
    percentages = {}
    for func in scores:
        if counts[func] > 0:
            max_score = 5 * counts[func]
            min_score = 1 * counts[func]
            normalized = (scores[func] - min_score) / (max_score - min_score) * 100
            percentages[func] = round(normalized)
        else:
            percentages[func] = 50

    # Sort functions by score to get stack
    sorted_functions = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)

    # Match to closest MBTI type based on function stack
    best_match = None
    best_score = -1

    for mbti_type, stack in MBTI_FUNCTION_STACKS.items():
        match_score = 0
        for i, func in enumerate(stack[:4]):  # Compare top 4 functions
            if i < len(sorted_functions):
                # Weight by position (dominant weighted more)
                weight = 4 - i
                if sorted_functions[i] == func:
                    match_score += weight * 2
                elif func in sorted_functions[:4]:
                    match_score += weight

        if match_score > best_score:
            best_score = match_score
            best_match = mbti_type

    # Create result showing top 4 functions
    result_type = '-'.join(sorted_functions[:4])

    return result_type, scores, percentages, best_match
