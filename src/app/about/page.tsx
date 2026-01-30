import Link from "next/link";

export default function AboutPage() {
  return (
    <div className="min-h-screen py-12 px-4">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold mb-4">About AoT</h1>
          <p className="text-xl text-slate-400">
            Academy of Tribes - Discover Your Tribe, Understand Yourself
          </p>
        </div>

        <div className="space-y-12">
          {/* Mission */}
          <section className="card">
            <h2 className="text-2xl font-semibold mb-4">Our Mission</h2>
            <p className="text-slate-300 leading-relaxed">
              The Academy of Tribes (AoT) helps you discover which personality tribe you belong to
              and how to connect with others. We believe that understanding our differences and
              similarities can provide profound insights into human behavior, team dynamics, and
              personal growth.
            </p>
          </section>

          {/* Why MBTI */}
          <section className="card">
            <h2 className="text-2xl font-semibold mb-4">Why MBTI?</h2>
            <p className="text-slate-300 leading-relaxed mb-6">
              The Myers-Briggs Type Indicator (MBTI) is based on Carl Jung&apos;s theory of psychological
              types. It provides a framework for understanding how people perceive the world and
              make decisions. While no personality assessment captures the full complexity of human
              nature, MBTI offers a useful starting point for self-reflection and understanding others.
            </p>
            <div className="grid md:grid-cols-2 gap-4">
              {[
                { title: "Self-Awareness", desc: "Understanding your type can help you recognize your natural strengths and blind spots." },
                { title: "Better Communication", desc: "Learn how different types prefer to communicate and process information." },
                { title: "Team Dynamics", desc: "Build more effective teams by understanding cognitive diversity." },
                { title: "Career Guidance", desc: "Explore careers that align with your natural preferences and strengths." },
              ].map((item, i) => (
                <div key={i} className="bg-slate-700/50 rounded-lg p-4">
                  <h3 className="font-semibold mb-2 text-indigo-400">{item.title}</h3>
                  <p className="text-slate-400 text-sm">{item.desc}</p>
                </div>
              ))}
            </div>
          </section>

          {/* Four Dimensions */}
          <section className="card">
            <h2 className="text-2xl font-semibold mb-6">The Four Dimensions</h2>
            <div className="space-y-6">
              {[
                { icon: "E/I", color: "from-rose-500 to-pink-500", title: "Energy Direction",
                  desc1: "Extraversion (E) - Energized by external world, action, people",
                  desc2: "Introversion (I) - Energized by internal world, reflection, ideas" },
                { icon: "S/N", color: "from-violet-500 to-indigo-500", title: "Information Gathering",
                  desc1: "Sensing (S) - Focus on concrete facts, details, present reality",
                  desc2: "Intuition (N) - Focus on patterns, possibilities, future potential" },
                { icon: "T/F", color: "from-emerald-500 to-teal-500", title: "Decision Making",
                  desc1: "Thinking (T) - Decide based on logic, objective analysis",
                  desc2: "Feeling (F) - Decide based on values, impact on people" },
                { icon: "J/P", color: "from-orange-500 to-amber-500", title: "Lifestyle Approach",
                  desc1: "Judging (J) - Prefer structure, planning, closure",
                  desc2: "Perceiving (P) - Prefer flexibility, spontaneity, options" },
              ].map((dim, i) => (
                <div key={i} className="flex gap-4">
                  <div className={`w-16 h-16 rounded-xl bg-gradient-to-br ${dim.color} flex items-center justify-center text-white font-bold text-lg shrink-0`}>
                    {dim.icon}
                  </div>
                  <div>
                    <h3 className="font-semibold mb-1">{dim.title}</h3>
                    <p className="text-slate-400 text-sm">{dim.desc1}</p>
                    <p className="text-slate-400 text-sm">{dim.desc2}</p>
                  </div>
                </div>
              ))}
            </div>
          </section>

          {/* Important Notes */}
          <section className="card bg-amber-900/20 border-amber-800">
            <h2 className="text-2xl font-semibold mb-4">Important Notes</h2>
            <ul className="space-y-3 text-slate-300">
              <li className="flex gap-2">
                <span className="text-amber-400">•</span>
                <span><strong>No type is better than another.</strong> Each has unique strengths and contributions.</span>
              </li>
              <li className="flex gap-2">
                <span className="text-amber-400">•</span>
                <span><strong>MBTI describes preferences, not abilities.</strong> You can develop skills outside your natural preferences.</span>
              </li>
              <li className="flex gap-2">
                <span className="text-amber-400">•</span>
                <span><strong>Your type is not a box.</strong> It&apos;s a starting point for understanding, not a limitation.</span>
              </li>
              <li className="flex gap-2">
                <span className="text-amber-400">•</span>
                <span><strong>Context matters.</strong> People may behave differently in different situations.</span>
              </li>
              <li className="flex gap-2">
                <span className="text-amber-400">•</span>
                <span><strong>This is a simplified assessment.</strong> For a comprehensive evaluation, consult a certified MBTI practitioner.</span>
              </li>
            </ul>
          </section>

          {/* Find Your Tribe */}
          <section className="card">
            <h2 className="text-2xl font-semibold mb-4">Find Your Tribe</h2>
            <p className="text-slate-300 leading-relaxed mb-4">
              AoT helps you understand yourself and connect with like-minded individuals.
              Our platform explores how personality insights can improve:
            </p>
            <ul className="space-y-2 text-slate-400 mb-6">
              <li className="flex gap-2"><span className="text-indigo-400">→</span> Team building and collaboration</li>
              <li className="flex gap-2"><span className="text-indigo-400">→</span> Personal relationships and communication</li>
              <li className="flex gap-2"><span className="text-indigo-400">→</span> Career development and job satisfaction</li>
              <li className="flex gap-2"><span className="text-indigo-400">→</span> Leadership and management styles</li>
              <li className="flex gap-2"><span className="text-indigo-400">→</span> Self-awareness and personal growth</li>
            </ul>
            <p className="text-slate-300">
              Join our community and discover the power of understanding personality types.
            </p>
          </section>
        </div>

        {/* CTA */}
        <div className="text-center py-12 mt-12 bg-gradient-to-r from-indigo-900/30 to-purple-900/30 rounded-2xl">
          <h2 className="text-2xl font-bold mb-4">Ready to explore?</h2>
          <div className="flex flex-wrap justify-center gap-4">
            <Link href="/quiz/mbti" className="btn btn-primary text-lg px-8 py-4">
              Take the Assessment
            </Link>
            <Link href="/types" className="btn btn-secondary text-lg px-8 py-4">
              Browse All Types
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
