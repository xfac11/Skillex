import click
from exerciseui import ExerciseUI
from exercisecatalog import ExerciseCatalog
@click.command()
@click.argument("exercise_id", type=str)
def view(exercise_id):
    """View one exercise using its id"""
    exercise_catalog = ExerciseCatalog()
    if not exercise_catalog.exists_table():
        click.echo("No exercise table exists. Please use the script in the scripts folder to download all exercises")
        return
    ui = ExerciseUI(exercise_catalog.get_exercise(exercise_id))
    click.echo(ui.to_string())