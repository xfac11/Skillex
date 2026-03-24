import click
from addtosleeplog import*
from config import load_config
from getuser import get_user
from saveusersleepstreak import save_user_sleep_streak
@click.command(help="Adds sleep hours to the log and updates your sleep streak")
@click.argument("sleep_hours", type=float)
def sleep(sleep_hours:float):
    name_id = load_config()
    if name_id is None:
        click.echo("No user found in the config file. Please use skillex init to initiate a user")
        return
    user = get_user(name_id[0])
    if user is None:
        click.echo("No user found in the database with that name. The config.json file might be corrupted")
        return
    
    if exists_sleep_log():
        if is_sleep_log_updated(user.id):
            click.echo("You have already logged sleep hours for today.")
            return
    
    add_sleep_log_entry(sleep_hours, user.id)
    
    if sleep_hours >= 7.0:
        click.echo("Good Job! You slept for 7 hours or more")
        if sleep_log_yesterday(user.id):
            click.echo(f"Your new sleep streak is {user.sleep_streak + 1}")
            save_user_sleep_streak(user, user.sleep_streak + 1)
            return
        click.echo("Unfourtanley you forgot to log yesterday so the streak is reset to 1")
        save_user_sleep_streak(user, 1)
        return
    else:
        if sleep_log_yesterday(user.id):
            new_sleep_streak = max(user.sleep_streak - 1)
            click.echo("You slept for less than 7 hours. Your streak is decreased by 1")
            click.echo(f"Your new streak is {new_sleep_streak}")
            save_user_sleep_streak(user, new_sleep_streak)
            return
        click.echo("Unfourtanley you forgot to log yesterday so the streak is reset to 1")
        save_user_sleep_streak(user, 1)
        return
            
        
    