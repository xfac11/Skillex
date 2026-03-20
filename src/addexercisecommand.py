import click
from searchexercise import search_exercise
from calculatexperience import create_exercise_experience
from addtolog import create_exercise
@click.command(help="Adds an exercise using its name. The name can be partailly right")
@click.argument("exercise")
def add(exercise):
    results = search_exercise(exercise)
    if len(results) == 0:
        click.echo("No exercise matches found. Use skillex search with a bodypart to find available exercises")
        return
    
    selected_exercise = None
    if len(results) == 1:
        selected_exercise = create_exercise(results[0][0])
    elif len(results) > 1:
        i = 0
        for exercise in results:
            click.echo(f"{i+1} {exercise[1]}")
            i += 1
        exercise_index = click.prompt("Select one exercise from the list. Enter 0 to abort", type=int)
        if exercise_index == 0:
            return
        selected_exercise = create_exercise(results[exercise_index-1][0])
    
    click.echo(f"Selected exercise {selected_exercise.name}")
    
    if selected_exercise.bodypart == "cardio":
        time = click.prompt("Enter in the duration of the exercise in minutes", type=int)
        distance = click.prompt("Enter in the distance in km", type=float)
        click.echo("1. Easy")
        click.echo("2. Medium")
        click.echo("3. Hard")
        effort = click.prompt("Select your effort", type=int)
        
    
        
    