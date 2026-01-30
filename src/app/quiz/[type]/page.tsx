"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { MBTI_QUESTIONS, calculateMBTI, MBTI_TYPES } from "@/lib/mbti";

export default function QuizPage({ params }: { params: { type: string } }) {
  const router = useRouter();
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState<Record<number, string>>({});
  const [showResults, setShowResults] = useState(false);
  const [result, setResult] = useState<{ type: string; percentages: Record<string, number> } | null>(null);

  const questions = MBTI_QUESTIONS;
  const progress = ((currentQuestion + 1) / questions.length) * 100;

  const handleAnswer = (choice: string) => {
    const newAnswers = { ...answers, [questions[currentQuestion].id]: choice };
    setAnswers(newAnswers);

    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      const calculatedResult = calculateMBTI(newAnswers);
      setResult(calculatedResult);
      setShowResults(true);
    }
  };

  const goBack = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  };

  if (showResults && result) {
    const typeInfo = MBTI_TYPES[result.type];
    return (
      <div className="min-h-screen py-12 px-4">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-12">
            <div className="inline-block px-4 py-2 bg-indigo-500/20 text-indigo-400 rounded-full text-sm font-medium mb-4">
              Your Personality Type
            </div>
            <div
              className="text-7xl font-bold mb-4"
              style={{ color: typeInfo.color }}
            >
              {result.type}
            </div>
            <h1 className="text-3xl font-bold mb-2">{typeInfo.title}</h1>
            <p className="text-slate-400 text-lg max-w-2xl mx-auto">{typeInfo.summary}</p>
          </div>

          {/* Dimension Bars */}
          <div className="card mb-8">
            <h2 className="text-xl font-semibold mb-6">Your Dimension Scores</h2>
            <div className="space-y-6">
              {[
                { left: "E", right: "I", leftLabel: "Extraversion", rightLabel: "Introversion" },
                { left: "S", right: "N", leftLabel: "Sensing", rightLabel: "Intuition" },
                { left: "T", right: "F", leftLabel: "Thinking", rightLabel: "Feeling" },
                { left: "J", right: "P", leftLabel: "Judging", rightLabel: "Perceiving" },
              ].map((dim) => (
                <div key={dim.left}>
                  <div className="flex justify-between text-sm mb-2">
                    <span className={result.percentages[dim.left] > 50 ? "text-indigo-400 font-semibold" : "text-slate-400"}>
                      {dim.leftLabel} ({dim.left})
                    </span>
                    <span className={result.percentages[dim.right] > 50 ? "text-purple-400 font-semibold" : "text-slate-400"}>
                      {dim.rightLabel} ({dim.right})
                    </span>
                  </div>
                  <div className="flex h-3 bg-slate-700 rounded-full overflow-hidden">
                    <div
                      className="bg-indigo-500 transition-all duration-500"
                      style={{ width: `${result.percentages[dim.left]}%` }}
                    />
                    <div
                      className="bg-purple-500 transition-all duration-500"
                      style={{ width: `${result.percentages[dim.right]}%` }}
                    />
                  </div>
                  <div className="flex justify-between text-xs text-slate-500 mt-1">
                    <span>{result.percentages[dim.left]}%</span>
                    <span>{result.percentages[dim.right]}%</span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Details Grid */}
          <div className="grid md:grid-cols-2 gap-6 mb-8">
            <div className="card">
              <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                <span className="text-yellow-400">★</span> Strengths
              </h3>
              <ul className="space-y-2">
                {typeInfo.strengths.map((s, i) => (
                  <li key={i} className="text-slate-300 flex items-center gap-2">
                    <span className="w-1.5 h-1.5 bg-green-400 rounded-full"></span>
                    {s}
                  </li>
                ))}
              </ul>
            </div>

            <div className="card">
              <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                <span className="text-orange-400">⚡</span> Challenges
              </h3>
              <ul className="space-y-2">
                {typeInfo.challenges.map((c, i) => (
                  <li key={i} className="text-slate-300 flex items-center gap-2">
                    <span className="w-1.5 h-1.5 bg-orange-400 rounded-full"></span>
                    {c}
                  </li>
                ))}
              </ul>
            </div>

            <div className="card">
              <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                <span className="text-blue-400">💼</span> Career Paths
              </h3>
              <ul className="space-y-2">
                {typeInfo.careers.map((c, i) => (
                  <li key={i} className="text-slate-300 flex items-center gap-2">
                    <span className="w-1.5 h-1.5 bg-blue-400 rounded-full"></span>
                    {c}
                  </li>
                ))}
              </ul>
            </div>

            <div className="card">
              <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                <span className="text-purple-400">👤</span> Famous People
              </h3>
              <ul className="space-y-2">
                {typeInfo.famous.map((f, i) => (
                  <li key={i} className="text-slate-300 flex items-center gap-2">
                    <span className="w-1.5 h-1.5 bg-purple-400 rounded-full"></span>
                    {f}
                  </li>
                ))}
              </ul>
            </div>
          </div>

          <div className="flex justify-center gap-4">
            <button
              onClick={() => {
                setShowResults(false);
                setCurrentQuestion(0);
                setAnswers({});
                setResult(null);
              }}
              className="btn btn-primary"
            >
              Retake Quiz
            </button>
            <button
              onClick={() => router.push("/types")}
              className="btn btn-secondary"
            >
              Explore All Types
            </button>
          </div>
        </div>
      </div>
    );
  }

  const question = questions[currentQuestion];

  return (
    <div className="min-h-screen py-12 px-4">
      <div className="max-w-2xl mx-auto">
        {/* Progress */}
        <div className="mb-8">
          <div className="flex justify-between text-sm text-slate-400 mb-2">
            <span>Question {currentQuestion + 1} of {questions.length}</span>
            <span>{Math.round(progress)}% complete</span>
          </div>
          <div className="h-2 bg-slate-700 rounded-full overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-indigo-500 to-purple-500 transition-all duration-300"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>

        {/* Question Card */}
        <div className="card">
          <h2 className="text-2xl font-semibold mb-8 text-center">
            {question.question}
          </h2>

          <div className="space-y-4">
            <button
              onClick={() => handleAnswer("A")}
              className={`w-full p-6 rounded-xl text-left transition-all duration-200 border-2 ${
                answers[question.id] === "A"
                  ? "border-indigo-500 bg-indigo-500/20"
                  : "border-slate-600 hover:border-slate-500 hover:bg-slate-700/50"
              }`}
            >
              <span className="font-semibold text-indigo-400 mr-2">A.</span>
              {question.option_a}
            </button>

            <button
              onClick={() => handleAnswer("B")}
              className={`w-full p-6 rounded-xl text-left transition-all duration-200 border-2 ${
                answers[question.id] === "B"
                  ? "border-purple-500 bg-purple-500/20"
                  : "border-slate-600 hover:border-slate-500 hover:bg-slate-700/50"
              }`}
            >
              <span className="font-semibold text-purple-400 mr-2">B.</span>
              {question.option_b}
            </button>
          </div>

          {currentQuestion > 0 && (
            <div className="mt-6 text-center">
              <button onClick={goBack} className="text-slate-400 hover:text-white transition">
                ← Previous Question
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
