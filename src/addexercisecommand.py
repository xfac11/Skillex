import click
from searchexercise import search_exercise
from calculatexperience import create_exercise_experience
from addtolog import create_exercise
from config import load_config
from effort import*
from getuser import get_user

def calculate_average_volume(user_id:int, exercise_id:str) -> int:
    """A volume means weight x reps x sets, the average volume within the last 30 days
        This will be calculated by taking at max 30 weight volume from the same exercise divided by 30
    """
    return 0

def get_highest_weight(user_id:int, exercise_id:str) -> int:
    """This is the highest weight used in this exercise. Look in the logs to retrieve the highest weight"""
    return 0

def calculate_average_speed(user_id:int, exercise_id:str) -> float:
    """This is the average speed calculated using the last 30 exercises of this type. """
    return 0
@click.command(help="Adds an exercise using its name. The name can be partailly right")
@click.argument("exercise")
def add(exercise):
    name_id = load_config()
    user = get_user(name_id[0])
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
    average_volume = calculate_average_volume(user.id, selected_exercise.id) 
    highest_weight = get_highest_weight(user.id, selected_exercise.id)
    exercise_avg_speed = calculate_average_speed(user.id, selected_exercise.id) 
    experience = create_exercise_experience(user.sleep_streak, repeats, sets, weight, average_volume, highest_weight, distance, time, effort.value, 1, exercise_avg_speed)
    
    click.echo(f"Experience gained: {experience.get_experience_points()}")
    
    level_gained = user.increase_global_xp(experience.get_experience_points())
    level_gained = user.increase_body_xp(selected_exercise.bodypart, experience.get_experience_points())
    
    
    
        
    
        
    