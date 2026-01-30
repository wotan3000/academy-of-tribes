# AoT Website - Academy of Tribes Personality Platform

A modern, responsive web application for personality assessments including MBTI, Big Five, Enneagram, DISC, and Cognitive Functions. Built as part of the Academy of Tribes (AoT) digital platform.

## Features

- **Multiple Assessments**: MBTI, Big Five (OCEAN), Enneagram, DISC, and Cognitive Functions
- **User Accounts**: Registration, login, profiles, and assessment history
- **Team Features**: Create teams, analyze team dynamics, invite members
- **Compatibility Analysis**: Compare personalities and get relationship insights
- **Gamification**: XP, levels, badges, and streaks
- **Modern UI**: Dark theme with smooth animations and responsive design
- **Shareable Results**: Unique URLs for sharing personality results

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
cd website
pip install -r requirements.txt
```

### Run Development Server

```bash
python app.py
```

Then open http://localhost:5000 in your browser.

### Production Deployment

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Project Structure

```
website/
├── app.py                 # Flask application & API routes
├── models.py              # SQLAlchemy database models
├── analysis.py            # Personality analysis engine
├── requirements.txt       # Python dependencies
├── assessments/           # Assessment modules
│   ├── __init__.py
│   ├── mbti.py           # Myers-Briggs Type Indicator
│   ├── big_five.py       # Big Five (OCEAN) personality
│   ├── enneagram.py      # Enneagram types
│   ├── disc.py           # DISC behavioral assessment
│   └── cognitive.py      # Jungian Cognitive Functions
├── static/
│   ├── css/
│   │   └── style.css     # Complete styling
│   └── js/
│       └── main.js       # Client-side interactivity
└── templates/
    ├── base.html         # Base template with nav/footer
    ├── index.html        # Home page
    ├── dashboard.html    # User dashboard
    ├── types.html        # All personality types
    ├── about.html        # About page
    ├── auth/             # Login/register templates
    ├── assessments/      # Quiz and results templates
    ├── teams/            # Team management templates
    ├── analysis/         # Insights and compatibility
    └── profile/          # User profile templates
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/dashboard` | GET | User dashboard |
| `/assessments` | GET | Assessment list |
| `/quiz/<type>` | GET | Take assessment |
| `/results/<id>` | GET | Results page |
| `/types` | GET | All personality types |
| `/teams` | GET | Team management |
| `/compatibility` | GET | Compatibility analysis |
| `/insights` | GET | Personal insights |
| `/api/submit/<type>` | POST | Submit quiz answers |
| `/api/results/<id>` | GET | Get result data |
| `/api/stats` | GET | Aggregate statistics |

## Technology Stack

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Frontend**: Vanilla JavaScript, CSS3
- **Database**: SQLite (development), PostgreSQL (production)
- **Fonts**: Inter, Space Grotesk (Google Fonts)

## License

Part of the Academy of Tribes project.
