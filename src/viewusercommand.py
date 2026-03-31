import click
from config import load_config
from userdatabase import UserDatabase
from user import User
from calculatexperience import calculate_global_level


@click.command(help="Shows your current stats")
def stats():
    name_id = load_config()
    if name_id is None:
        click.echo("No user found in the config file. Please use skillex init to initiate a user")
        return
    user_db = UserDatabase()
    user:User = user_db.get_user(name_id[0])
    if user is None:
        click.echo("No user found in the database with that name. The config.json file might be corrupted")
        return
    
    click.echo(f"---{user.name}---")
    click.echo(f"Level {calculate_global_level(user.global_xp)} Sleep streak {user.sleep_streak} days")
    click.echo("-------------------------------------------------")
    
    i = 0
    print_string = ""
    for key in user.body_xp.get_bodyparts():
        bodypart_text = key.replace("_", " ").capitalize()
        bodypart_text = "{:<10}".format(bodypart_text)
        print_string += f"|{bodypart_text} {user.body_xp.get_bodypart_level(key)}/99"
        i += 1
        if i == 3:
            click.echo(print_string + "|")
            print_string = ""
            i = 0
    click.echo("-------------------------------------------------")
    
    
    
    