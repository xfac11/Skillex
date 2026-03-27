import click
from addtosleeplog import*
from config import load_config
from getuser import get_user
from saveusersleepstreak import save_user_sleep_streak

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
    user = get_user(name_id[0])
    if user is None:
        click.echo("No user found in the database with that name. The config.json file might be corrupted")
        return
    
    if exists_sleep_log():
        if is_sleep_log_updated(user.id):
            click.echo("You have already logged sleep hours for today.")
            return
    
    add_sleep_log_entry(sleep_hours, user.id)
    
    codes = update_sleep_streak(user, sleep_hours, sleep_log_yesterday(user.id))
    save_user_sleep_streak(user, user.sleep_streak)
    
    print_sleep_streak_update(user, codes)
    
    
    
            
        
    