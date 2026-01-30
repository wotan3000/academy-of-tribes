import Link from "next/link";

const assessments = [
  {
    key: "mbti",
    name: "Myers-Briggs Type Indicator",
    shortName: "MBTI",
    description: "Discover your 4-letter personality type across extraversion, intuition, thinking, and judging dimensions.",
    questions: 24,
    time: "5-10 min",
    icon: "◆",
    color: "#6366f1",
    available: true,
  },
  {
    key: "big-five",
    name: "Big Five Personality",
    shortName: "OCEAN",
    description: "Measure your openness, conscientiousness, extraversion, agreeableness, and neuroticism.",
    questions: 25,
    time: "5-10 min",
    icon: "★",
    color: "#10b981",
    available: false,
  },
  {
    key: "enneagram",
    name: "Enneagram",
    shortName: "9 Types",
    description: "Discover your core personality type among nine interconnected types.",
    questions: 27,
    time: "8-12 min",
    icon: "◯",
    color: "#f59e0b",
    available: false,
  },
  {
    key: "disc",
    name: "DISC Assessment",
    shortName: "DISC",
    description: "Understand your behavioral style: Dominance, Influence, Steadiness, Conscientiousness.",
    questions: 20,
    time: "5-8 min",
    icon: "▲",
    color: "#ef4444",
    available: false,
  },
  {
    key: "cognitive",
    name: "Cognitive Functions",
    shortName: "8 Functions",
    description: "Explore your cognitive function stack based on Jungian psychology.",
    questions: 32,
    time: "10-15 min",
    icon: "◈",
    color: "#8b5cf6",
    available: false,
  },
];

export default function AssessmentsPage() {
  return (
    <div className="min-h-screen py-12 px-4">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold mb-4">Personality Assessments</h1>
          <p className="text-slate-400 text-lg">
            Choose an assessment to discover more about yourself
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {assessments.map((assessment) => (
            <div
              key={assessment.key}
              className={`card relative overflow-hidden ${!assessment.available && "opacity-60"}`}
            >
              <div
                className="absolute top-0 right-0 w-32 h-32 -mr-8 -mt-8 rounded-full opacity-20"
                style={{ backgroundColor: assessment.color }}
              />
              <div className="relative">
                <div
                  className="w-14 h-14 rounded-xl flex items-center justify-center text-2xl mb-4"
                  style={{ backgroundColor: `${assessment.color}20`, color: assessment.color }}
                >
                  {assessment.icon}
                </div>
                <div className="text-xs text-slate-500 mb-1">{assessment.shortName}</div>
                <h3 className="text-xl font-semibold mb-2">{assessment.name}</h3>
                <p className="text-slate-400 text-sm mb-4">{assessment.description}</p>
                <div className="flex items-center gap-4 text-sm text-slate-500 mb-4">
                  <span>{assessment.questions} questions</span>
                  <span>•</span>
                  <span>{assessment.time}</span>
                </div>
                {assessment.available ? (
                  <Link
                    href={`/quiz/${assessment.key}`}
                    className="btn btn-primary w-full justify-center"
                  >
                    Start Assessment
                  </Link>
                ) : (
                  <button
                    disabled
                    className="btn bg-slate-700 text-slate-400 w-full justify-center cursor-not-allowed"
                  >
                    Coming Soon
                  </button>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
