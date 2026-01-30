import Link from "next/link";

const typeCards = [
  { code: "INTJ", color: "#6366f1" }, { code: "INTP", color: "#8b5cf6" },
  { code: "ENTJ", color: "#ec4899" }, { code: "ENTP", color: "#f43f5e" },
  { code: "INFJ", color: "#10b981" }, { code: "INFP", color: "#14b8a6" },
  { code: "ENFJ", color: "#22c55e" }, { code: "ENFP", color: "#84cc16" },
  { code: "ISTJ", color: "#0ea5e9" }, { code: "ISFJ", color: "#06b6d4" },
  { code: "ESTJ", color: "#3b82f6" }, { code: "ESFJ", color: "#2563eb" },
  { code: "ISTP", color: "#f97316" }, { code: "ISFP", color: "#fb923c" },
  { code: "ESTP", color: "#ef4444" }, { code: "ESFP", color: "#f87171" },
];

export default function Home() {
  return (
    <div>
      {/* Hero Section */}
      <section className="py-20 px-4">
        <div className="max-w-7xl mx-auto grid lg:grid-cols-2 gap-12 items-center">
          <div>
            <div className="inline-block px-4 py-2 bg-indigo-500/20 text-indigo-400 rounded-full text-sm font-medium mb-6">
              MBTI Personality Assessment
            </div>
            <h1 className="text-5xl lg:text-6xl font-bold mb-6">
              Discover Your <span className="gradient-text">Personality Type</span>
            </h1>
            <p className="text-xl text-slate-400 mb-8">
              Uncover your unique cognitive patterns and understand how you perceive
              and interact with the world around you.
            </p>
            <div className="flex flex-wrap gap-4">
              <Link href="/quiz/mbti" className="btn btn-primary text-lg px-8 py-4">
                Start Assessment
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </Link>
              <Link href="/types" className="btn btn-secondary text-lg px-8 py-4">
                Explore Types
              </Link>
            </div>
            <div className="flex gap-8 mt-12">
              <div>
                <div className="text-3xl font-bold text-white">16</div>
                <div className="text-slate-400">Personality Types</div>
              </div>
              <div>
                <div className="text-3xl font-bold text-white">24</div>
                <div className="text-slate-400">Questions</div>
              </div>
              <div>
                <div className="text-3xl font-bold text-white">5</div>
                <div className="text-slate-400">Assessments</div>
              </div>
            </div>
          </div>
          <div className="grid grid-cols-4 gap-3">
            {typeCards.map((type) => (
              <div
                key={type.code}
                className="aspect-square rounded-lg flex items-center justify-center text-white font-bold text-sm hover:scale-105 transition-transform cursor-pointer"
                style={{ backgroundColor: type.color }}
              >
                {type.code}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="py-20 px-4 bg-slate-900/50">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold mb-4">How It Works</h2>
            <p className="text-slate-400">A scientifically-informed assessment to help you understand your personality</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            {[
              { title: "Answer Questions", desc: "Respond to 24 carefully crafted questions about your preferences and behaviors.", icon: "✓" },
              { title: "Get Your Type", desc: "Discover your 4-letter personality type across four key dimensions.", icon: "◆" },
              { title: "Understand Yourself", desc: "Learn about your strengths, challenges, ideal careers, and more.", icon: "★" },
            ].map((item, i) => (
              <div key={i} className="card text-center">
                <div className="w-16 h-16 rounded-full bg-indigo-500/20 flex items-center justify-center text-2xl text-indigo-400 mx-auto mb-4">
                  {item.icon}
                </div>
                <h3 className="text-xl font-semibold mb-2">{item.title}</h3>
                <p className="text-slate-400">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Four Dimensions */}
      <section className="py-20 px-4">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold mb-4">The Four Dimensions</h2>
            <p className="text-slate-400">MBTI measures your preferences across four pairs of traits</p>
          </div>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              { left: "E", right: "I", title: "Extraversion / Introversion", desc: "How you gain energy: from external activities and people, or from inner reflection and solitude." },
              { left: "S", right: "N", title: "Sensing / Intuition", desc: "How you gather information: through concrete facts and details, or through patterns and possibilities." },
              { left: "T", right: "F", title: "Thinking / Feeling", desc: "How you make decisions: through logical analysis, or through values and how others are affected." },
              { left: "J", right: "P", title: "Judging / Perceiving", desc: "How you approach life: with structure and planning, or with flexibility and spontaneity." },
            ].map((dim, i) => (
              <div key={i} className="card">
                <div className="flex items-center justify-center gap-4 mb-4">
                  <span className="text-2xl font-bold text-indigo-400">{dim.left}</span>
                  <span className="text-slate-500">vs</span>
                  <span className="text-2xl font-bold text-purple-400">{dim.right}</span>
                </div>
                <h3 className="text-lg font-semibold mb-2 text-center">{dim.title}</h3>
                <p className="text-slate-400 text-sm text-center">{dim.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 px-4 bg-gradient-to-r from-indigo-900/50 to-purple-900/50">
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-3xl font-bold mb-4">Ready to Discover Your Type?</h2>
          <p className="text-slate-400 mb-8">The assessment takes about 5-10 minutes to complete.</p>
          <Link href="/quiz/mbti" className="btn btn-primary text-lg px-8 py-4">
            Begin Assessment
          </Link>
        </div>
      </section>
    </div>
  );
}
