import click
from searchcommand import search
from bodypartscommand import bodyparts
from pathlib import Path

DATABASE_PATH = Path("skillex.db")

def check_database():
    """Checks if the skillex database existst"""
    return DATABASE_PATH.is_file()
    
@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name) -> None:
    """Greets NAME for COUNT times."""
    if check_database():
        click.echo("Not synced to the external database. Run scripts/sync_exercises.py from the skillex folder")
        return
    for _ in range(count):
        click.echo(f"Hello, {name}!")

@click.group()
def cli() -> None:
    """An exercise tracker CLI using gamification"""
    pass
        
cli.add_command(hello)
cli.add_command(search)
cli.add_command(bodyparts)

if __name__ == "__main__":
    cli()
