import click
from pathlib import Path

DATABASE_PATH = Path("skillex.db")

def check_database():
    """Checks if the skillex database existst"""
    return DATABASE_PATH.is_file()
    
    

@click.group()
def skillex():
    """An exercise tracker CLI using gamification"""
    pass


@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Greets NAME for COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    skillex()
