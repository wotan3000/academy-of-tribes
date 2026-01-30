# Academy of Tribes - Personality Assessment Platform

A modern Next.js web application for personality assessments including MBTI, Big Five, Enneagram, DISC, and Cognitive Functions.

## Features

- **Multiple Assessments**: MBTI (live), Big Five, Enneagram, DISC, Cognitive Functions (coming soon)
- **24-Question MBTI Quiz**: Comprehensive assessment covering all four dimensions
- **Instant Results**: Real-time personality type calculation with visual breakdowns
- **All 16 Types**: Complete descriptions, strengths, challenges, and career suggestions
- **Modern UI**: Dark theme with Tailwind CSS and smooth animations
- **Responsive Design**: Works on desktop and mobile

## Quick Start

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Production Build

```bash
npm run build
npm start
```

## Project Structure

```
├── src/
│   ├── app/
│   │   ├── page.tsx          # Home page
│   │   ├── layout.tsx        # Root layout with nav/footer
│   │   ├── globals.css       # Global styles
│   │   ├── about/            # About page
│   │   ├── assessments/      # Assessments list
│   │   ├── quiz/[type]/      # Dynamic quiz pages
│   │   └── types/            # All personality types
│   └── lib/
│       └── mbti.ts           # MBTI questions, types & calculator
├── public/                   # Static assets
└── package.json
```

## Technology Stack

- **Framework**: Next.js 16 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS 4
- **Fonts**: Inter, Space Grotesk (Google Fonts)

## Deploy on Vercel

This app is optimized for deployment on [Vercel](https://vercel.com).

```bash
npm i -g vercel
vercel
```

## License

Academy of Tribes Project
