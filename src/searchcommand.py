import click

from exercisecatalog import ExerciseCatalog
from exercise import Exercise

def format_exercise(exercise:Exercise):
    return f"{exercise.id} | {exercise.name}"


@click.command()
@click.argument("query")
@click.option("--pager", "-p", is_flag=True, help="If set it uses a pager when more than 15 were found")
@click.option("--bodypart", "-b", help="Searches for the specific bodypart. Use bodyparts command for a list of bodyparts")
def search(query:str, pager:bool, bodypart:str):
    """
    Searches for exercises and echoes their name and id. 
    Can use exact name or id or partial name.
    If more than 15 were found a pager starts
    """
    exercise_catalog = ExerciseCatalog()
    if not exercise_catalog.exists_table():
        click.echo("No exercises found in the database.")
        click.echo("Please run the sync_exercises.py script in the scripts folder to download the exercises")
        return
    
    exercises = None
    if bodypart:
        exercises = exercise_catalog.search_exercise_bodypart(query, bodypart, True)
    else:
        exercises = exercise_catalog.search_exercise(query, True)
    
    if exercises is None:
        click.echo("No exercises were found.")
        return
    
    if len(exercises) <= 15:
        for exercise in exercises:
            click.echo(f"{exercise.id} | {exercise.name}")
        return
    
    
    exercise_str = list(map(format_exercise, exercises))
    exercise_str = "\n".join(exercise_str)
    if pager:
        click.echo_via_pager(exercise_str)
    else:
        click.echo(exercise_str)
    
    