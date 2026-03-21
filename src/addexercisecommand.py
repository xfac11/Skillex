import click
from searchexercise import search_exercise
from calculatexperience import create_exercise_experience
from addtolog import create_exercise
from effort import*
@click.command(help="Adds an exercise using its name. The name can be partailly right")
@click.argument("exercise")
def add(exercise):
    results = search_exercise(exercise, True)
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
    
    
    time = click.prompt("Enter in the duration of the exercise in minutes", type=int)
    distance = click.prompt("Enter in the distance in km", type=float)
    click.echo("1. Easy")
    click.echo("2. Medium")
    click.echo("3. Hard")
    effort_level = click.prompt("Select your effort", type=int)
    effort = Effort(EffortLevel(effort_level))
    repeats = click.prompt("Enter in the number of repeats", type=int)
    sets = click.prompt("Enter in the number of sets", type=int)
    weight = click.prompt("Enter in the weight used in kg", type=float)
    average_volume = 60 ##This will be calculated by taking at max 30 weight volume from the same exercise divided by 30
    highest_weight = 100 ##This is the highest weight used in this exercise. Look in the logs to retrieve the highest weight
    exercise_avg_speed = 20 ##This is the average speed calculated using the last 30 exercises of this type. So 
    experience = create_exercise_experience(1, repeats, sets, weight, average_volume, highest_weight, distance, time, effort.value, 1, exercise_avg_speed)
    
    experience.get_experience_points()
        
    
        
    