# SoDev Levelling

A gamified coding progress tracker that helps developers track their learning journey through quests and experience points.

## Project Structure

```
SoDev Levelling/
├── source/
│   ├── __init__.py
│   ├── config.py           # Configuration settings
│   ├── main.py             # Main entry point
│   ├── api/                # API endpoints
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── cli/                # Command-line interface
│   │   ├── __init__.py
│   │   └── commands.py
│   ├── db/                 # Database models and connections
│   │   ├── __init__.py
│   │   └── models.py
│   └── core/               # Core business logic
│       ├── __init__.py
│       └── progress.py
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Make sure MongoDB is running locally on the default port (27017).

## Usage

### Command Line Interface

Run the CLI:
```
python -m source.main
```

Available commands:
- `add-quest`: Add a new coding quest
- `list-quests`: List all available quests
- `complete-quest`: Mark a quest as completed and gain XP
- `show-progress`: Show current XP and level
- `serve`: Start the API server

### API

Start the API server:
```
python -m source.main serve
```

API Endpoints:
- `POST /quests/`: Create a new quest
- `GET /quests/`: Get all quests
- `PATCH /quests/{quest_id}`: Complete a quest
- `GET /progress`: Get current progress

## Configuration

Edit `source/config.py` to change:
- MongoDB connection settings
- Leveling thresholds
- API host and port