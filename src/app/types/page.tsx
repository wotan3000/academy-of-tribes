import Link from "next/link";
import { MBTI_TYPES } from "@/lib/mbti";

const typeGroups = [
  {
    name: "Analysts",
    description: "Intuitive (N) and Thinking (T) types, known for their rationality and impartiality",
    types: ["INTJ", "INTP", "ENTJ", "ENTP"],
  },
  {
    name: "Diplomats",
    description: "Intuitive (N) and Feeling (F) types, known for their empathy and idealism",
    types: ["INFJ", "INFP", "ENFJ", "ENFP"],
  },
  {
    name: "Sentinels",
    description: "Sensing (S) and Judging (J) types, known for their practicality and order",
    types: ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
  },
  {
    name: "Explorers",
    description: "Sensing (S) and Perceiving (P) types, known for their spontaneity and flexibility",
    types: ["ISTP", "ISFP", "ESTP", "ESFP"],
  },
];

export default function TypesPage() {
  return (
    <div className="min-h-screen py-12 px-4">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold mb-4">The 16 Personality Types</h1>
          <p className="text-slate-400 text-lg">
            Explore all MBTI personality types and learn about their characteristics
          </p>
        </div>

        {typeGroups.map((group) => (
          <div key={group.name} className="mb-12">
            <div className="mb-6">
              <h2 className="text-2xl font-bold mb-2">{group.name}</h2>
              <p className="text-slate-400">{group.description}</p>
            </div>
            <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
              {group.types.map((code) => {
                const type = MBTI_TYPES[code];
                return (
                  <div
                    key={code}
                    className="card hover:border-slate-600 transition-all duration-200 group"
                  >
                    <div
                      className="text-3xl font-bold mb-2"
                      style={{ color: type.color }}
                    >
                      {code}
                    </div>
                    <h3 className="text-lg font-semibold mb-2">{type.title}</h3>
                    <p className="text-slate-400 text-sm mb-4 line-clamp-2">
                      {type.summary}
                    </p>
                    <div className="space-y-2 text-sm">
                      <div>
                        <span className="text-slate-500">Strengths:</span>{" "}
                        <span className="text-slate-300">
                          {type.strengths.slice(0, 3).join(", ")}
                        </span>
                      </div>
                      <div>
                        <span className="text-slate-500">Careers:</span>{" "}
                        <span className="text-slate-300">
                          {type.careers.slice(0, 3).join(", ")}
                        </span>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        ))}

        <div className="text-center py-12 bg-gradient-to-r from-indigo-900/30 to-purple-900/30 rounded-2xl">
          <h2 className="text-2xl font-bold mb-4">Want to know your type?</h2>
          <p className="text-slate-400 mb-6">
            Take our 24-question assessment to discover your personality type.
          </p>
          <Link href="/quiz/mbti" className="btn btn-primary text-lg px-8 py-4">
            Take the Quiz
          </Link>
        </div>
      </div>
    </div>
  );
}
