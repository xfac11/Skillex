import click
from exerciselog import ExerciseLog
from config import load_config
from userdatabase import UserDatabase
from logui import LogUI
import datetime
@click.command()
@click.option("--exercise_id", "exercise_id", type=str, default=None, help="Show only this type of exercise when printing the log. Can be found by search")
@click.option("--days", "days", type=int, default=0, help="Show only this number of days in the past")
def log(exercise_id, days):
    """Shows a log of all exercises done"""
    name_id = load_config()
    if name_id is None:
        click.echo("No user found in the config file. Call init to create a user")
        return
    
    user_db = UserDatabase()
    user = user_db.get_user(name_id[0])
    if user is None:
        click.echo("No user found in the database. Config might be corrupted or you need to use init to create a user")
        return
    
    exercise_log = ExerciseLog(user.id)
    entries = exercise_log.get_days(days, exercise_id)
    if len(entries) == 0:
        click.echo("No entries in the log. Start exercising and add them with skillex add")
        return
    log_ui = LogUI(entries)
    click.echo(log_ui.to_string())
    
        
        