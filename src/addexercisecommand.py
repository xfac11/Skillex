import click
from exercisecatalog import ExerciseCatalog
from exerciselogentry import ExerciseLogEntry
from calculatexperience import*
from exerciselog import ExerciseLog
from config import load_config
from effort import*
from userdatabase import UserDatabase
from selector import Selector
import datetime
@click.command(help="Adds an exercise using its name. The name can be partailly right")
@click.argument("exercise")
def add(exercise):
    exercise_catalog = ExerciseCatalog()
    if not exercise_catalog.exists_table():
        click.echo("No exercises found in the database.")
        click.echo("Please run the sync_exercises.py script in the scripts folder to download the exercises")
        return
    name_id = load_config()
    if name_id is None:
        click.echo("No user found in the config file. Please use skillex init to initiate a user")
        return
    
    
    
    user_db = UserDatabase()
    if not user_db.exists():
        click.echo("No user has been added to the database. Please use skillex init to initiate a user")
        return
    user = user_db.get_user(name_id[0])

    if user is None:
        click.echo("No user found in the database with that name. The config.json file might be corrupted")
        return
    exercise_log = ExerciseLog(user.id)
    results = exercise_catalog.search_exercise(exercise, True)
    if len(results) == 0:
        click.echo("No exercise matches found. Use skillex search with a bodypart to find available exercises")
        return
    
    selected_exercise = None
    if len(results) == 1:
        selected_exercise = results[0]
    elif len(results) > 1:
        exercise_selector = Selector("Select one exercise.", results)
        exercise = exercise_selector.select()
        if not exercise:
            return
        selected_exercise = exercise
    
    click.echo(f"Selected exercise {click.style(selected_exercise.name, fg='green')}")
    
    
    time = click.prompt("Enter in the duration of the exercise in minutes", type=int)
    while time <= 0:
        time = click.prompt("Enter a valid time that is more than 0 or press B to abort)", type=int)
    distance = click.prompt("Enter in the distance in km", type=float)
    selector = Selector("Select your effort", [EffortLevel.EASY, EffortLevel.NORMAL, EffortLevel.HARD])
    effort_level = selector.select()
    effort = Effort(EffortLevel(effort_level))
    repeats = click.prompt("Enter in the number of repeats", type=int)
    sets = click.prompt("Enter in the number of sets", type=int)
    weight = click.prompt("Enter in the weight used in kg", type=float)
    average_volume = exercise_log.get_average_weight_volume(selected_exercise.id) 
    highest_weight = exercise_log.get_highest_weight(selected_exercise.id)
    exercise_avg_speed = exercise_log.get_average_speed(selected_exercise.id) 
    experience = create_exercise_experience(user.sleep_streak, repeats, sets, weight, average_volume, highest_weight, distance, time, effort.value, 1, exercise_avg_speed)
    
    
    global_level = user.increase_global_xp(experience.get_experience_points())    
    body_level = user.increase_body_xp(selected_exercise.bodypart.replace(" ", "_"), experience.get_experience_points())
    
    exercise_log.add(selected_exercise, datetime.datetime.now().timestamp(), experience.get_experience_points(), repeats*sets*weight, distance / (time / 60), weight)
    
    user_db.save_user(user)
    
    click.echo(f"{selected_exercise.bodypart.capitalize()}++ {experience.get_experience_points()}xp")
    click.echo(f"Global++ {experience.get_experience_points()}xp")
    click.echo()
    if global_level > 0:
        click.echo("Level up!")
        click.echo(f"Global Level {global_level - 1} --> Level {global_level}")
        click.echo()
    
    if body_level > 0:
        click.echo("Level up!")
        click.echo(f"{selected_exercise.bodypart.capitalize()} Level {body_level - 1} --> Level {body_level}")
        click.echo()
    
    
    global_progress = calculate_global_progress_to_next(user.global_xp)
    body_progress = calculate_body_progress_to_next(user.body_xp.get_bodypart_xp(selected_exercise.bodypart.replace(" ", "_")))
    
    global_progress_text = ""
    for i in range(int(global_progress*20)):
        global_progress_text += "█"
    for i in range(int(global_progress*20), 20):
        global_progress_text += " "
    
    click.echo(f"Global progress to next level")
    click.echo(f"|{global_progress_text}|")
    click.echo()
    body_progress_text = ""
    for i in range(int(body_progress*20)):
        body_progress_text += "█"
    for i in range(int(body_progress*20), 20):
        body_progress_text += " "
    
    click.echo(f"{selected_exercise.bodypart.capitalize()} progress to next level")
    click.echo(f"|{body_progress_text}|")
    
    
    
    
    
    
    
        
    
        
    