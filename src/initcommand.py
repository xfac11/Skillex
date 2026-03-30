import click
from config import save_config
from userdatabase import UserDatabase
from user import User
from bodyparts import BodyParts
@click.command()
def init():
    click.echo("Welcome to Skillex!")
    click.echo("Skillex tracks exercises using commands and tracks your sleep")
    click.echo("Gain xp and level up you and your body")
    click.echo()
    name = click.prompt("Enter in your name")
    user_db = UserDatabase("skillex.db")
    if not user_db.add_user(User(-1, name, 0, BodyParts(), 0, 0, 0)):
        click.echo("Something went wrong when adding a user with this name")
        click.echo("Choose a different name. Aborting")
        return
    
    user = user_db.get_user(name)
    if user is None:
        click.echo("Something went wrong when retreiving the user. Aborting")
    if not save_config(user.name, user.id):
        click.echo("Something went wrong when writing to config.json. Aborting")
        return
    
    click.echo("Now your exercise journey can begin!")
    click.echo("Start by using the add command with an exercise name as an argument")
    
    