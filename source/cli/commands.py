import typer
import asyncio

from source.db.models import Quest
from source.api.routes import create_quest, get_quests, complete_quest as api_complete_quest, get_progress as api_get_progress

cli = typer.Typer()

@cli.command()
def add_quest(title: str, description: str, difficulty: str):
    """Add a new coding quest."""
    asyncio.run(create_quest(Quest(title=title, description=description, difficulty=difficulty)))
    typer.echo("Quest added successfully!")

@cli.command()
def list_quests():
    """List all available quests."""
    quests = asyncio.run(get_quests())
    for q in quests:
        typer.echo(f"[{q.difficulty}] {q.title} - {'Completed' if q.completed else 'Pending'}")

@cli.command()
def complete_quest(quest_id: str):
    """Mark a quest as completed and gain XP."""
    result = asyncio.run(api_complete_quest(quest_id))
    typer.echo(f"{result['message']} - XP: {result['current_xp']}, Level: {result['level']}")

@cli.command()
def show_progress():
    """Show current XP and level."""
    progress = asyncio.run(api_get_progress())
    typer.echo(f"XP: {progress['xp']}, Level: {progress['level']}")