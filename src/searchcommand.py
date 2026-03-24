import click

from searchexercise import search_exercise
from searchexercise import search_exercise_bodypart
from existsexercisetable import exists_exercise_table

def format_exercise_tuple(exercise_tuple):
    return f"{exercise_tuple[0]} | {exercise_tuple[1]}"


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
    
    if not exists_exercise_table():
        click.echo("No exercises found in the database.")
        click.echo("Please run the sync_exercises.py script in the scripts folder to download the exercises")
        return
    
    exercises = None
    if bodypart:
        exercises = search_exercise_bodypart(query, bodypart, True)
    else:
        exercises = search_exercise(query, True)
    
    if exercises is None:
        click.echo("No exercises were found.")
        return
    
    if len(exercises) <= 15:
        for exercise in exercises:
            click.echo(f"{exercise[0]} | {exercise[1]}")
        return
    
    
    exercise_str = list(map(format_exercise_tuple, exercises))
    exercise_str = "\n".join(exercise_str)
    if pager:
        click.echo_via_pager(exercise_str)
    else:
        click.echo(exercise_str)
    
    