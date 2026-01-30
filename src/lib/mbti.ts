export const MBTI_QUESTIONS = [
  { id: 1, question: "At a party, you tend to:", option_a: "Interact with many people, including strangers", option_b: "Interact with a few people you know well", dimension: ["E", "I"] },
  { id: 2, question: "You are more impressed by:", option_a: "Principles and theories", option_b: "Facts and data", dimension: ["N", "S"] },
  { id: 3, question: "When making decisions, you typically:", option_a: "Consider logic and consistency first", option_b: "Consider people's feelings first", dimension: ["T", "F"] },
  { id: 4, question: "You prefer to:", option_a: "Have things decided and settled", option_b: "Keep your options open", dimension: ["J", "P"] },
  { id: 5, question: "In social situations, you:", option_a: "Start conversations easily", option_b: "Wait for others to approach you", dimension: ["E", "I"] },
  { id: 6, question: "You are more interested in:", option_a: "What could be possible", option_b: "What is actual and present", dimension: ["N", "S"] },
  { id: 7, question: "You find it more natural to:", option_a: "Be objective and impersonal", option_b: "Be personal and empathetic", dimension: ["T", "F"] },
  { id: 8, question: "You prefer work that involves:", option_a: "Following a clear schedule", option_b: "Flexibility and variety", dimension: ["J", "P"] },
  { id: 9, question: "After being with a group of people, you feel:", option_a: "Energized and stimulated", option_b: "Drained and need alone time", dimension: ["E", "I"] },
  { id: 10, question: "You are more drawn to:", option_a: "Abstract ideas and concepts", option_b: "Concrete facts and details", dimension: ["N", "S"] },
  { id: 11, question: "In conflicts, you tend to prioritize:", option_a: "Finding the truth", option_b: "Maintaining harmony", dimension: ["T", "F"] },
  { id: 12, question: "You prefer to:", option_a: "Make detailed plans in advance", option_b: "Be spontaneous and adaptable", dimension: ["J", "P"] },
  { id: 13, question: "When meeting new people, you:", option_a: "Easily share about yourself", option_b: "Keep things to yourself initially", dimension: ["E", "I"] },
  { id: 14, question: "You trust more:", option_a: "Your imagination and hunches", option_b: "Your direct observations", dimension: ["N", "S"] },
  { id: 15, question: "You are more likely to:", option_a: "Analyze pros and cons logically", option_b: "Follow your heart", dimension: ["T", "F"] },
  { id: 16, question: "You prefer:", option_a: "Structured environments", option_b: "Flexible environments", dimension: ["J", "P"] },
  { id: 17, question: "You would rather:", option_a: "Discuss ideas in a group", option_b: "Think through ideas alone", dimension: ["E", "I"] },
  { id: 18, question: "You are more interested in:", option_a: "Future possibilities", option_b: "Present realities", dimension: ["N", "S"] },
  { id: 19, question: "When giving feedback, you:", option_a: "Focus on what needs improvement", option_b: "Focus on encouragement first", dimension: ["T", "F"] },
  { id: 20, question: "Deadlines make you feel:", option_a: "Motivated and organized", option_b: "Stressed and constrained", dimension: ["J", "P"] },
  { id: 21, question: "You recharge by:", option_a: "Being around others", option_b: "Spending time alone", dimension: ["E", "I"] },
  { id: 22, question: "You prefer learning through:", option_a: "Theories and concepts", option_b: "Hands-on experience", dimension: ["N", "S"] },
  { id: 23, question: "You value more:", option_a: "Justice and fairness", option_b: "Mercy and compassion", dimension: ["T", "F"] },
  { id: 24, question: "You are more comfortable when:", option_a: "Things are planned and organized", option_b: "Things are open-ended", dimension: ["J", "P"] },
];

export const MBTI_TYPES: Record<string, { title: string; summary: string; color: string; strengths: string[]; challenges: string[]; careers: string[]; famous: string[] }> = {
  INTJ: {
    title: "The Architect",
    summary: "Strategic thinkers with a plan for everything. INTJs are imaginative and strategic, with a natural ability to turn ideas into action.",
    color: "#6366f1",
    strengths: ["Strategic thinking", "Independent", "Determined", "Innovative", "High standards"],
    challenges: ["Can be overly critical", "Dismissive of emotions", "Perfectionist", "Impatient"],
    careers: ["Scientist", "Engineer", "Lawyer", "Architect", "Investment Banker"],
    famous: ["Elon Musk", "Michelle Obama", "Isaac Newton", "Friedrich Nietzsche"]
  },
  INTP: {
    title: "The Logician",
    summary: "Innovative inventors with an unquenchable thirst for knowledge. INTPs are logical, original, and creative thinkers.",
    color: "#8b5cf6",
    strengths: ["Analytical", "Objective", "Creative", "Honest", "Open-minded"],
    challenges: ["Insensitive", "Absent-minded", "Condescending", "Overthinking"],
    careers: ["Software Developer", "Professor", "Scientist", "Mathematician", "Technical Writer"],
    famous: ["Albert Einstein", "Bill Gates", "Marie Curie", "Charles Darwin"]
  },
  ENTJ: {
    title: "The Commander",
    summary: "Bold, imaginative leaders who always find a way. ENTJs are natural leaders who are confident and assertive.",
    color: "#ec4899",
    strengths: ["Efficient", "Energetic", "Self-confident", "Strong-willed", "Strategic"],
    challenges: ["Stubborn", "Intolerant", "Impatient", "Arrogant"],
    careers: ["CEO", "Entrepreneur", "Lawyer", "Management Consultant", "University Professor"],
    famous: ["Steve Jobs", "Margaret Thatcher", "Napoleon Bonaparte", "Franklin D. Roosevelt"]
  },
  ENTP: {
    title: "The Debater",
    summary: "Smart and curious thinkers who cannot resist an intellectual challenge. ENTPs are innovative and entrepreneurial.",
    color: "#f43f5e",
    strengths: ["Knowledgeable", "Quick thinker", "Charismatic", "Energetic", "Original"],
    challenges: ["Argumentative", "Insensitive", "Intolerant", "Unfocused"],
    careers: ["Entrepreneur", "Lawyer", "Consultant", "Creative Director", "Engineer"],
    famous: ["Mark Twain", "Thomas Edison", "Leonardo da Vinci", "Socrates"]
  },
  INFJ: {
    title: "The Advocate",
    summary: "Quiet and mystical, yet very inspiring and tireless idealists. INFJs are creative nurturers with a strong sense of personal integrity.",
    color: "#10b981",
    strengths: ["Creative", "Insightful", "Principled", "Passionate", "Altruistic"],
    challenges: ["Sensitive", "Perfectionist", "Private", "Burnout-prone"],
    careers: ["Counselor", "Writer", "Teacher", "Healthcare Worker", "HR Manager"],
    famous: ["Martin Luther King Jr.", "Nelson Mandela", "Mother Teresa", "Carl Jung"]
  },
  INFP: {
    title: "The Mediator",
    summary: "Poetic, kind, and altruistic, always eager to help a good cause. INFPs are imaginative idealists guided by their core values.",
    color: "#14b8a6",
    strengths: ["Idealistic", "Empathetic", "Open-minded", "Creative", "Passionate"],
    challenges: ["Unrealistic", "Self-isolating", "Too idealistic", "Emotionally vulnerable"],
    careers: ["Writer", "Counselor", "Artist", "Musician", "Psychologist"],
    famous: ["William Shakespeare", "J.R.R. Tolkien", "Princess Diana", "Johnny Depp"]
  },
  ENFJ: {
    title: "The Protagonist",
    summary: "Charismatic and inspiring leaders who are able to mesmerize their listeners. ENFJs are warm and forthright.",
    color: "#22c55e",
    strengths: ["Tolerant", "Reliable", "Charismatic", "Altruistic", "Natural leaders"],
    challenges: ["Overly idealistic", "Too selfless", "Sensitive to criticism", "Indecisive"],
    careers: ["Teacher", "HR Director", "Sales Manager", "Counselor", "Public Relations"],
    famous: ["Barack Obama", "Oprah Winfrey", "Martin Luther King Jr.", "John Cusack"]
  },
  ENFP: {
    title: "The Campaigner",
    summary: "Enthusiastic, creative, and sociable free spirits who can always find a reason to smile.",
    color: "#84cc16",
    strengths: ["Curious", "Enthusiastic", "Excellent communicators", "Creative", "Popular"],
    challenges: ["Unfocused", "Disorganized", "Overly optimistic", "Overthinking"],
    careers: ["Journalist", "Actor", "Consultant", "Counselor", "Entrepreneur"],
    famous: ["Robin Williams", "Robert Downey Jr.", "Will Smith", "Ellen DeGeneres"]
  },
  ISTJ: {
    title: "The Logistician",
    summary: "Practical and fact-minded individuals whose reliability cannot be doubted.",
    color: "#0ea5e9",
    strengths: ["Honest", "Direct", "Responsible", "Calm", "Practical"],
    challenges: ["Stubborn", "Insensitive", "Judgmental", "Resistant to change"],
    careers: ["Accountant", "Military Officer", "Lawyer", "Judge", "Detective"],
    famous: ["George Washington", "Warren Buffett", "Queen Elizabeth II", "Angela Merkel"]
  },
  ISFJ: {
    title: "The Defender",
    summary: "Very dedicated and warm protectors, always ready to defend their loved ones.",
    color: "#06b6d4",
    strengths: ["Supportive", "Reliable", "Patient", "Observant", "Loyal"],
    challenges: ["Shy", "Take things personally", "Overload themselves", "Reluctant to change"],
    careers: ["Nurse", "Teacher", "Social Worker", "Administrator", "Counselor"],
    famous: ["Queen Elizabeth II", "Beyoncé", "Kate Middleton", "Halle Berry"]
  },
  ESTJ: {
    title: "The Executive",
    summary: "Excellent administrators, unsurpassed at managing things or people.",
    color: "#3b82f6",
    strengths: ["Dedicated", "Strong-willed", "Direct", "Honest", "Loyal"],
    challenges: ["Inflexible", "Stubborn", "Judgmental", "Difficulty relaxing"],
    careers: ["Business Administrator", "Manager", "Police Officer", "Judge", "Financial Officer"],
    famous: ["John D. Rockefeller", "Frank Sinatra", "Judge Judy", "Lyndon B. Johnson"]
  },
  ESFJ: {
    title: "The Consul",
    summary: "Extraordinarily caring, social, and popular, always eager to help.",
    color: "#2563eb",
    strengths: ["Strong practical skills", "Loyal", "Warm", "Responsible", "Good at connecting"],
    challenges: ["Worried about social status", "Inflexible", "Needy", "Selfless to a fault"],
    careers: ["Healthcare Worker", "Teacher", "Social Worker", "Sales Representative", "HR Specialist"],
    famous: ["Taylor Swift", "Bill Clinton", "Jennifer Garner", "Danny Glover"]
  },
  ISTP: {
    title: "The Virtuoso",
    summary: "Bold and practical experimenters, masters of all kinds of tools.",
    color: "#f97316",
    strengths: ["Optimistic", "Creative", "Practical", "Spontaneous", "Rational"],
    challenges: ["Stubborn", "Insensitive", "Private", "Easily bored"],
    careers: ["Mechanic", "Engineer", "Forensic Scientist", "Pilot", "Programmer"],
    famous: ["Clint Eastwood", "Michael Jordan", "Tom Cruise", "Bear Grylls"]
  },
  ISFP: {
    title: "The Adventurer",
    summary: "Flexible and charming artists, always ready to explore and experience something new.",
    color: "#fb923c",
    strengths: ["Charming", "Sensitive", "Imaginative", "Passionate", "Artistic"],
    challenges: ["Fiercely independent", "Unpredictable", "Easily stressed", "Overly competitive"],
    careers: ["Artist", "Designer", "Veterinarian", "Forest Ranger", "Chef"],
    famous: ["Michael Jackson", "Marilyn Monroe", "Lana Del Rey", "Bob Dylan"]
  },
  ESTP: {
    title: "The Entrepreneur",
    summary: "Smart, energetic, and very perceptive, who truly enjoy living on the edge.",
    color: "#ef4444",
    strengths: ["Bold", "Rational", "Direct", "Sociable", "Perceptive"],
    challenges: ["Impatient", "Risk-prone", "Unstructured", "Insensitive"],
    careers: ["Entrepreneur", "Marketing Director", "Paramedic", "Police Officer", "Sales"],
    famous: ["Ernest Hemingway", "Jack Nicholson", "Eddie Murphy", "Madonna"]
  },
  ESFP: {
    title: "The Entertainer",
    summary: "Spontaneous, energetic, and enthusiastic entertainers who love life.",
    color: "#f87171",
    strengths: ["Bold", "Original", "Practical", "Observant", "Excellent people skills"],
    challenges: ["Sensitive", "Conflict-averse", "Unfocused", "Poor planners"],
    careers: ["Event Planner", "Sales Representative", "Trip Planner", "Actor", "Designer"],
    famous: ["Marilyn Monroe", "Elvis Presley", "Jamie Oliver", "Adele"]
  }
};

export function calculateMBTI(answers: Record<number, string>): { type: string; percentages: Record<string, number> } {
  const scores: Record<string, number> = { E: 0, I: 0, S: 0, N: 0, T: 0, F: 0, J: 0, P: 0 };

  MBTI_QUESTIONS.forEach((q) => {
    const answer = answers[q.id];
    if (answer === "A") {
      scores[q.dimension[0]]++;
    } else if (answer === "B") {
      scores[q.dimension[1]]++;
    }
  });

  const pairs = [["E", "I"], ["S", "N"], ["T", "F"], ["J", "P"]];
  const percentages: Record<string, number> = {};
  let type = "";

  pairs.forEach(([a, b]) => {
    const total = scores[a] + scores[b];
    percentages[a] = total > 0 ? Math.round((scores[a] / total) * 100) : 50;
    percentages[b] = total > 0 ? Math.round((scores[b] / total) * 100) : 50;
    type += scores[a] >= scores[b] ? a : b;
  });

  return { type, percentages };
}
