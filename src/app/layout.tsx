import type { Metadata } from "next";
import { Inter, Space_Grotesk } from "next/font/google";
import "./globals.css";
import Link from "next/link";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
const spaceGrotesk = Space_Grotesk({ subsets: ["latin"], variable: "--font-space" });

export const metadata: Metadata = {
  title: "AoT - Academy of Tribes",
  description: "Discover your personality tribe. Take assessments for MBTI, Big Five, Enneagram, and more.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${inter.variable} ${spaceGrotesk.variable} font-sans antialiased`}>
        <nav className="bg-slate-900/80 backdrop-blur-md border-b border-slate-800 sticky top-0 z-50">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex items-center justify-between h-16">
              <Link href="/" className="flex items-center gap-2">
                <span className="text-2xl text-indigo-400">▲</span>
                <span className="text-xl font-bold text-white">AoT</span>
              </Link>
              <div className="hidden md:flex items-center gap-8">
                <Link href="/" className="text-slate-300 hover:text-white transition">Home</Link>
                <Link href="/assessments" className="text-slate-300 hover:text-white transition">Take Quiz</Link>
                <Link href="/types" className="text-slate-300 hover:text-white transition">Personality Types</Link>
                <Link href="/about" className="text-slate-300 hover:text-white transition">About</Link>
              </div>
            </div>
          </div>
        </nav>

        <main className="min-h-screen">
          {children}
        </main>

        <footer className="bg-slate-900 border-t border-slate-800 py-12">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="grid md:grid-cols-3 gap-8">
              <div>
                <h4 className="text-lg font-semibold mb-4">AoT - Academy of Tribes</h4>
                <p className="text-slate-400">Discover your tribe. Understand yourself and others.</p>
              </div>
              <div>
                <h4 className="text-lg font-semibold mb-4">Quick Links</h4>
                <ul className="space-y-2 text-slate-400">
                  <li><Link href="/assessments" className="hover:text-white transition">MBTI Quiz</Link></li>
                  <li><Link href="/types" className="hover:text-white transition">Personality Types</Link></li>
                  <li><Link href="/about" className="hover:text-white transition">About Us</Link></li>
                </ul>
              </div>
              <div>
                <h4 className="text-lg font-semibold mb-4">Resources</h4>
                <ul className="space-y-2 text-slate-400">
                  <li><a href="#" className="hover:text-white transition">Documentation</a></li>
                  <li><a href="#" className="hover:text-white transition">Research</a></li>
                  <li><a href="#" className="hover:text-white transition">Contact</a></li>
                </ul>
              </div>
            </div>
            <div className="border-t border-slate-800 mt-8 pt-8 text-center text-slate-500">
              <p>&copy; 2025 Academy of Tribes. All rights reserved.</p>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
