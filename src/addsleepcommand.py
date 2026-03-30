import click
from sleeplog import SleepLog
from config import load_config
from user import User
from userdatabase import UserDatabase
from user import SleepUpdateCode
def print_sleep_streak_update(user:User, codes:list[SleepUpdateCode]) -> None:
    for code in codes:
        match code:
            case SleepUpdateCode.SLEPT_7:
                click.echo("Good Job! You slept for 7 hours or more")
            case SleepUpdateCode.SLEPT_LESS_7:
                click.echo("You slept for less than 7 hours. Your streak is decreased by 1")
                click.echo(f"Your new streak is {user.sleep_streak}")
            case SleepUpdateCode.LOGGED_YESTERDAY:
                click.echo(f"Your new sleep streak is {user.sleep_streak}")
            case SleepUpdateCode.FORGOT_YESTERDAY:
                click.echo("Unfourtanley you forgot to log yesterday so the streak is reset to 1")

@click.command(help="Adds sleep hours to the log and updates your sleep streak")
@click.argument("sleep_hours", type=float)
def sleep(sleep_hours:float):
    name_id = load_config()
    if name_id is None:
        click.echo("No user found in the config file. Please use skillex init to initiate a user")
        return
    user_db = UserDatabase()
    user = user_db.get_user(name_id[0])
    if user is None:
        click.echo("No user found in the database with that name. The config.json file might be corrupted")
        return
    
    sleep_log = SleepLog(user.id)
    
    if sleep_log.exists():
        if sleep_log.is_sleep_logged(user.id):
            click.echo("You have already logged sleep hours for today.")
            return
    
    sleep_log.add_sleep_log_entry(sleep_hours)
    
    codes = user.update_sleep_streak(sleep_hours, sleep_log.has_logged_yesterday())
    
    user_db.save_user(user)
    
    print_sleep_streak_update(user, codes)
    
    
    
            
        
    