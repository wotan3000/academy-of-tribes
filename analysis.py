"""
AoT (Academy of Tribes) - Personality Analysis & Insights Engine
Advanced compatibility analysis, growth recommendations, and AI insights
"""

import math
from typing import Dict, List, Tuple, Optional
from assessments.mbti import MBTI_DESCRIPTIONS
from assessments.enneagram import ENNEAGRAM_DESCRIPTIONS


# ============================================================================
# MBTI Compatibility Analysis
# ============================================================================

MBTI_COMPATIBILITY = {
    # Ideal matches (high compatibility)
    'ideal': [
        ('INFJ', 'ENFP'), ('INFJ', 'ENTP'),
        ('INTJ', 'ENFP'), ('INTJ', 'ENTP'),
        ('INFP', 'ENFJ'), ('INFP', 'ENTJ'),
        ('INTP', 'ENTJ'), ('INTP', 'ENFJ'),
        ('ENFP', 'INFJ'), ('ENFP', 'INTJ'),
        ('ENTP', 'INFJ'), ('ENTP', 'INTJ'),
        ('ENFJ', 'INFP'), ('ENFJ', 'INTP'),
        ('ENTJ', 'INFP'), ('ENTJ', 'INTP'),
        ('ISFJ', 'ESFP'), ('ISFJ', 'ESTP'),
        ('ISTJ', 'ESFP'), ('ISTJ', 'ESTP'),
        ('ESFJ', 'ISFP'), ('ESFJ', 'ISTP'),
        ('ESTJ', 'ISFP'), ('ESTJ', 'ISTP'),
    ],
    # Good matches
    'good': [
        ('INFJ', 'INFP'), ('INFJ', 'ENFJ'),
        ('INTJ', 'INTP'), ('INTJ', 'ENTJ'),
        ('INFP', 'INFJ'), ('INFP', 'ENFP'),
        ('INTP', 'INTJ'), ('INTP', 'ENTP'),
        ('ENFP', 'INFP'), ('ENFP', 'ENFJ'),
        ('ENTP', 'INTP'), ('ENTP', 'ENTJ'),
        ('ENFJ', 'INFJ'), ('ENFJ', 'ENFP'),
        ('ENTJ', 'INTJ'), ('ENTJ', 'ENTP'),
    ],
}


def calculate_mbti_compatibility(type1: str, type2: str) -> Dict:
    """
    Calculate compatibility between two MBTI types
    Returns score (0-100) and detailed analysis
    """
    # Check for ideal/good matches
    pair = tuple(sorted([type1, type2]))
    reverse_pair = (type2, type1)

    if pair in MBTI_COMPATIBILITY['ideal'] or reverse_pair in MBTI_COMPATIBILITY['ideal']:
        base_score = 85
    elif pair in MBTI_COMPATIBILITY['good'] or reverse_pair in MBTI_COMPATIBILITY['good']:
        base_score = 75
    else:
        base_score = 60

    # Calculate function compatibility
    shared_functions = 0
    complementary_functions = 0

    # Compare dichotomies
    matching_dichotomies = sum(1 for a, b in zip(type1, type2) if a == b)

    # Adjust score based on similarities/differences
    if matching_dichotomies == 4:  # Same type
        base_score = 70  # Same types understand but may lack growth
    elif matching_dichotomies == 0:  # Opposite types
        base_score = max(base_score, 65)  # Can be challenging but complementary

    # Generate analysis
    strengths = []
    challenges = []
    tips = []

    # E/I analysis
    if type1[0] == type2[0]:
        if type1[0] == 'E':
            strengths.append("Both energized by social interaction")
        else:
            strengths.append("Both value quiet time and deep conversation")
    else:
        strengths.append("Balance between social engagement and reflection")
        challenges.append("Different social energy needs")
        tips.append("Respect each other's need for solitude or socializing")

    # S/N analysis
    if type1[1] == type2[1]:
        if type1[1] == 'S':
            strengths.append("Shared practical, detail-oriented approach")
        else:
            strengths.append("Shared love of ideas and possibilities")
    else:
        challenges.append("Different approaches to information (concrete vs abstract)")
        tips.append("Appreciate what the other brings - practical grounding or big-picture thinking")

    # T/F analysis
    if type1[2] == type2[2]:
        if type1[2] == 'T':
            strengths.append("Both value logic in decision-making")
        else:
            strengths.append("Both prioritize harmony and values")
    else:
        challenges.append("Different decision-making styles (logic vs values)")
        tips.append("Recognize both perspectives are valid - logic AND feelings matter")

    # J/P analysis
    if type1[3] == type2[3]:
        if type1[3] == 'J':
            strengths.append("Both prefer structure and planning")
        else:
            strengths.append("Both value flexibility and spontaneity")
    else:
        challenges.append("Different lifestyle preferences (planned vs spontaneous)")
        tips.append("Find middle ground between structure and flexibility")

    return {
        'score': min(100, base_score + (matching_dichotomies * 2)),
        'type1': type1,
        'type2': type2,
        'strengths': strengths,
        'challenges': challenges,
        'tips': tips,
        'summary': generate_compatibility_summary(type1, type2, base_score),
    }


def generate_compatibility_summary(type1: str, type2: str, score: int) -> str:
    """Generate a natural language summary of compatibility"""
    desc1 = MBTI_DESCRIPTIONS.get(type1, {}).get('title', type1)
    desc2 = MBTI_DESCRIPTIONS.get(type2, {}).get('title', type2)

    if score >= 85:
        return f"The {desc1} and {desc2} often form a natural, complementary partnership with excellent potential for understanding and growth."
    elif score >= 75:
        return f"The {desc1} and {desc2} share enough common ground to connect well while offering different perspectives that can enrich the relationship."
    elif score >= 65:
        return f"The {desc1} and {desc2} have moderate compatibility. Success requires mutual respect and understanding of differences."
    else:
        return f"The {desc1} and {desc2} may face challenges but can build a strong relationship through conscious effort and appreciation of differences."


# ============================================================================
# Team Dynamics Analysis
# ============================================================================

def analyze_team_dynamics(team_types: List[str]) -> Dict:
    """
    Analyze team composition and provide insights
    """
    if not team_types:
        return {'error': 'No team members'}

    # Count type distributions
    e_count = sum(1 for t in team_types if t[0] == 'E')
    i_count = len(team_types) - e_count
    s_count = sum(1 for t in team_types if t[1] == 'S')
    n_count = len(team_types) - s_count
    t_count = sum(1 for t in team_types if t[2] == 'T')
    f_count = len(team_types) - t_count
    j_count = sum(1 for t in team_types if t[3] == 'J')
    p_count = len(team_types) - j_count

    total = len(team_types)

    # Calculate diversity score
    balance_score = 100 - (
        abs(e_count - i_count) * 5 +
        abs(s_count - n_count) * 5 +
        abs(t_count - f_count) * 5 +
        abs(j_count - p_count) * 5
    )
    balance_score = max(0, balance_score)

    # Identify team strengths and gaps
    strengths = []
    gaps = []

    if e_count > total * 0.6:
        strengths.append("Strong external communication and energy")
    elif i_count > total * 0.6:
        strengths.append("Strong focus and deep thinking capacity")
        gaps.append("May need more external communication")

    if n_count > total * 0.6:
        strengths.append("Excellent at innovation and big-picture thinking")
        gaps.append("May overlook practical details")
    elif s_count > total * 0.6:
        strengths.append("Strong practical execution and attention to detail")
        gaps.append("May miss innovative opportunities")

    if t_count > total * 0.6:
        strengths.append("Strong analytical decision-making")
        gaps.append("May overlook team morale and feelings")
    elif f_count > total * 0.6:
        strengths.append("Strong team cohesion and values alignment")
        gaps.append("May struggle with tough objective decisions")

    if j_count > total * 0.6:
        strengths.append("Excellent at planning and meeting deadlines")
        gaps.append("May be inflexible with changing requirements")
    elif p_count > total * 0.6:
        strengths.append("Highly adaptable and responsive to change")
        gaps.append("May struggle with deadlines and structure")

    # Type distribution by temperament
    analysts = [t for t in team_types if t[1] == 'N' and t[2] == 'T']  # NT
    diplomats = [t for t in team_types if t[1] == 'N' and t[2] == 'F']  # NF
    sentinels = [t for t in team_types if t[1] == 'S' and t[3] == 'J']  # SJ
    explorers = [t for t in team_types if t[1] == 'S' and t[3] == 'P']  # SP

    return {
        'balance_score': balance_score,
        'distribution': {
            'E_I': {'E': e_count, 'I': i_count},
            'S_N': {'S': s_count, 'N': n_count},
            'T_F': {'T': t_count, 'F': f_count},
            'J_P': {'J': j_count, 'P': p_count},
        },
        'temperaments': {
            'analysts': len(analysts),
            'diplomats': len(diplomats),
            'sentinels': len(sentinels),
            'explorers': len(explorers),
        },
        'strengths': strengths,
        'gaps': gaps,
        'recommendations': generate_team_recommendations(team_types, gaps),
    }


def generate_team_recommendations(team_types: List[str], gaps: List[str]) -> List[str]:
    """Generate actionable recommendations for team improvement"""
    recommendations = []

    # General recommendations
    if len(set(team_types)) < len(team_types) * 0.5:
        recommendations.append("Consider adding more cognitive diversity to the team")

    if len(team_types) > 5 and len(gaps) > 2:
        recommendations.append("Assign specific roles to cover identified gaps")

    # Specific gap-based recommendations
    for gap in gaps:
        if "practical details" in gap.lower():
            recommendations.append("Assign a detail-oriented team member to review deliverables")
        elif "communication" in gap.lower():
            recommendations.append("Schedule regular external stakeholder check-ins")
        elif "morale" in gap.lower():
            recommendations.append("Include team-building and recognition activities")
        elif "deadlines" in gap.lower():
            recommendations.append("Implement structured project milestones")

    return recommendations[:5]  # Return top 5


# ============================================================================
# Growth & Development Recommendations
# ============================================================================

def generate_growth_recommendations(mbti_type: str, enneagram_type: Optional[str] = None) -> Dict:
    """
    Generate personalized growth recommendations based on personality types
    """
    mbti_desc = MBTI_DESCRIPTIONS.get(mbti_type, {})

    recommendations = {
        'focus_areas': mbti_desc.get('growth_areas', []),
        'practices': [],
        'books': [],
        'habits': [],
        'relationships': [],
    }

    # MBTI-based recommendations
    if mbti_type[0] == 'I':
        recommendations['practices'].append("Practice initiating conversations with new people weekly")
        recommendations['habits'].append("Schedule regular social activities to prevent isolation")
    else:
        recommendations['practices'].append("Schedule daily quiet reflection time")
        recommendations['habits'].append("Practice listening more than speaking in conversations")

    if mbti_type[1] == 'N':
        recommendations['practices'].append("Ground ideas in practical action steps")
        recommendations['habits'].append("Pay attention to present-moment details")
    else:
        recommendations['practices'].append("Explore 'what if' scenarios regularly")
        recommendations['habits'].append("Read about future trends and possibilities")

    if mbti_type[2] == 'T':
        recommendations['practices'].append("Ask 'How will this affect people?' before deciding")
        recommendations['habits'].append("Express appreciation to others daily")
        recommendations['relationships'].append("Practice validating others' feelings before problem-solving")
    else:
        recommendations['practices'].append("Make a pros/cons list for important decisions")
        recommendations['habits'].append("Set objective criteria before evaluating options")
        recommendations['relationships'].append("Be direct about your needs rather than hinting")

    if mbti_type[3] == 'J':
        recommendations['practices'].append("Leave unscheduled time for spontaneity")
        recommendations['habits'].append("Practice saying 'yes' to unexpected opportunities")
    else:
        recommendations['practices'].append("Create and follow a morning routine")
        recommendations['habits'].append("Use a calendar to track commitments")

    # Book recommendations based on type
    book_recommendations = {
        'INTJ': ["Thinking, Fast and Slow - Daniel Kahneman", "Good to Great - Jim Collins"],
        'INTP': ["Gödel, Escher, Bach - Douglas Hofstadter", "The Structure of Scientific Revolutions - Thomas Kuhn"],
        'ENTJ': ["The 7 Habits of Highly Effective People - Stephen Covey", "Principles - Ray Dalio"],
        'ENTP': ["Zero to One - Peter Thiel", "The Lean Startup - Eric Ries"],
        'INFJ': ["Man's Search for Meaning - Viktor Frankl", "Quiet - Susan Cain"],
        'INFP': ["The Alchemist - Paulo Coelho", "Big Magic - Elizabeth Gilbert"],
        'ENFJ': ["How to Win Friends and Influence People - Dale Carnegie", "Leaders Eat Last - Simon Sinek"],
        'ENFP': ["The Artist's Way - Julia Cameron", "Designing Your Life - Bill Burnett"],
        'ISTJ': ["Deep Work - Cal Newport", "Atomic Habits - James Clear"],
        'ISFJ': ["The 5 Love Languages - Gary Chapman", "Boundaries - Henry Cloud"],
        'ESTJ': ["Extreme Ownership - Jocko Willink", "The Effective Executive - Peter Drucker"],
        'ESFJ': ["Emotional Intelligence - Daniel Goleman", "Give and Take - Adam Grant"],
        'ISTP': ["Zen and the Art of Motorcycle Maintenance - Robert Pirsig", "The Craftsman - Richard Sennett"],
        'ISFP': ["The War of Art - Steven Pressfield", "Steal Like an Artist - Austin Kleon"],
        'ESTP': ["The 4-Hour Workweek - Tim Ferriss", "Never Split the Difference - Chris Voss"],
        'ESFP': ["The Happiness Project - Gretchen Rubin", "Year of Yes - Shonda Rhimes"],
    }

    recommendations['books'] = book_recommendations.get(mbti_type, [])

    return recommendations


# ============================================================================
# Communication Style Guide
# ============================================================================

def get_communication_guide(type1: str, type2: str) -> Dict:
    """
    Generate a communication guide between two types
    """
    guide = {
        'from_type1_to_type2': [],
        'from_type2_to_type1': [],
        'general_tips': [],
    }

    desc1 = MBTI_DESCRIPTIONS.get(type1, {})
    desc2 = MBTI_DESCRIPTIONS.get(type2, {})

    # E/I communication
    if type1[0] == 'E' and type2[0] == 'I':
        guide['from_type1_to_type2'].append("Give them time to process before expecting a response")
        guide['from_type1_to_type2'].append("Don't mistake their silence for disinterest")
        guide['from_type2_to_type1'].append("Let them think out loud without taking it as final")
        guide['from_type2_to_type1'].append("Engage verbally even when you prefer to reflect")
    elif type1[0] == 'I' and type2[0] == 'E':
        guide['from_type1_to_type2'].append("Share your thoughts verbally, not just in writing")
        guide['from_type1_to_type2'].append("Engage in their need for external processing")
        guide['from_type2_to_type1'].append("Pause and let them finish their thoughts")
        guide['from_type2_to_type1'].append("Don't fill every silence with conversation")

    # S/N communication
    if type1[1] == 'S' and type2[1] == 'N':
        guide['from_type1_to_type2'].append("Be open to their abstract ideas and theories")
        guide['from_type1_to_type2'].append("Ask about the big picture, not just details")
        guide['from_type2_to_type1'].append("Provide concrete examples and specifics")
        guide['from_type2_to_type1'].append("Connect ideas to practical applications")
    elif type1[1] == 'N' and type2[1] == 'S':
        guide['from_type1_to_type2'].append("Ground your ideas in concrete examples")
        guide['from_type1_to_type2'].append("Focus on what's relevant now, not just future possibilities")
        guide['from_type2_to_type1'].append("Be open to exploring possibilities and 'what ifs'")
        guide['from_type2_to_type1'].append("Ask about the meaning behind the details")

    # T/F communication
    if type1[2] == 'T' and type2[2] == 'F':
        guide['from_type1_to_type2'].append("Acknowledge their feelings before offering solutions")
        guide['from_type1_to_type2'].append("Express appreciation and warmth directly")
        guide['from_type2_to_type1'].append("Don't take their directness personally")
        guide['from_type2_to_type1'].append("Present concerns with logical reasoning")
    elif type1[2] == 'F' and type2[2] == 'T':
        guide['from_type1_to_type2'].append("Lead with logic and evidence when persuading")
        guide['from_type1_to_type2'].append("Don't take their critiques as personal rejection")
        guide['from_type2_to_type1'].append("Consider how your words affect them emotionally")
        guide['from_type2_to_type1'].append("Show that you value the relationship, not just the task")

    # General tips
    guide['general_tips'] = [
        f"Remember: {type1}s value {desc1.get('communication', 'clear communication')}",
        f"Remember: {type2}s value {desc2.get('communication', 'clear communication')}",
        "When in conflict, assume positive intent from the other person",
        "Appreciate what your differences bring to the relationship",
    ]

    return guide


# ============================================================================
# Topological Personality Space (TDA Integration)
# ============================================================================

def calculate_personality_coordinates(percentages: Dict) -> Dict:
    """
    Map personality percentages to a coordinate system for visualization
    Uses TDA-inspired dimensionality for personality space
    """
    # Extract MBTI percentages
    e_i = percentages.get('E', 50) - 50  # -50 to +50 scale
    s_n = percentages.get('S', 50) - 50
    t_f = percentages.get('T', 50) - 50
    j_p = percentages.get('J', 50) - 50

    # Map to 3D coordinates using dimensional reduction
    # This creates a personality "manifold"
    x = (e_i + s_n) / 100  # Action orientation
    y = (t_f + j_p) / 100  # Decision structure
    z = (e_i - j_p + s_n - t_f) / 200  # Cognitive style

    # Calculate personality "density" (how extreme the preferences are)
    density = math.sqrt(e_i**2 + s_n**2 + t_f**2 + j_p**2) / 100

    return {
        'x': round(x, 3),
        'y': round(y, 3),
        'z': round(z, 3),
        'density': round(density, 3),
        'raw_percentages': percentages,
    }


def find_personality_neighbors(user_coords: Dict, all_coords: List[Dict], n: int = 5) -> List[Dict]:
    """
    Find the n nearest neighbors in personality space
    Uses Euclidean distance in the personality manifold
    """
    def distance(c1, c2):
        return math.sqrt(
            (c1['x'] - c2['x'])**2 +
            (c1['y'] - c2['y'])**2 +
            (c1['z'] - c2['z'])**2
        )

    distances = [
        {'coords': c, 'distance': distance(user_coords, c)}
        for c in all_coords
        if c != user_coords
    ]

    distances.sort(key=lambda x: x['distance'])
    return distances[:n]


# ============================================================================
# Personality Evolution Tracking
# ============================================================================

def analyze_personality_evolution(results_history: List[Dict]) -> Dict:
    """
    Analyze how someone's personality results have changed over time
    """
    if len(results_history) < 2:
        return {'insufficient_data': True}

    # Sort by date
    sorted_results = sorted(results_history, key=lambda x: x['created_at'])

    # Track changes in each dimension
    changes = {
        'E_I': [],
        'S_N': [],
        'T_F': [],
        'J_P': [],
    }

    type_changes = []
    prev_type = None

    for result in sorted_results:
        pct = result.get('percentages', {})

        changes['E_I'].append(pct.get('E', 50))
        changes['S_N'].append(pct.get('S', 50))
        changes['T_F'].append(pct.get('T', 50))
        changes['J_P'].append(pct.get('J', 50))

        current_type = result.get('result_type')
        if prev_type and current_type != prev_type:
            type_changes.append({
                'from': prev_type,
                'to': current_type,
                'date': result['created_at'],
            })
        prev_type = current_type

    # Calculate trends
    def calculate_trend(values):
        if len(values) < 2:
            return 'stable'
        change = values[-1] - values[0]
        if change > 10:
            return 'increasing'
        elif change < -10:
            return 'decreasing'
        return 'stable'

    trends = {
        'extraversion': calculate_trend(changes['E_I']),
        'sensing': calculate_trend(changes['S_N']),
        'thinking': calculate_trend(changes['T_F']),
        'judging': calculate_trend(changes['J_P']),
    }

    # Consistency score
    consistency = 100 - (len(type_changes) * 10)
    consistency = max(0, consistency)

    return {
        'total_assessments': len(sorted_results),
        'type_changes': type_changes,
        'trends': trends,
        'consistency_score': consistency,
        'current_type': sorted_results[-1].get('result_type'),
        'first_type': sorted_results[0].get('result_type'),
        'insight': generate_evolution_insight(trends, type_changes),
    }


def generate_evolution_insight(trends: Dict, type_changes: List) -> str:
    """Generate insight about personality evolution"""
    if not type_changes:
        return "Your personality type has remained consistent, indicating stable self-awareness."

    changing_dimensions = [k for k, v in trends.items() if v != 'stable']

    if not changing_dimensions:
        return "While your overall type has shifted, your dimensional preferences have remained relatively balanced."

    insights = []
    if 'extraversion' in changing_dimensions:
        if trends['extraversion'] == 'increasing':
            insights.append("You've become more outgoing and socially energized over time")
        else:
            insights.append("You've become more introspective and internally focused")

    if 'thinking' in changing_dimensions:
        if trends['thinking'] == 'increasing':
            insights.append("Your decision-making has become more analytical")
        else:
            insights.append("You've become more attuned to values and feelings in decisions")

    return ". ".join(insights) + "." if insights else "Your personality shows interesting evolution patterns."
