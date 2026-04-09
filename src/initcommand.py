import click
from config import save_config
from userdatabase import UserDatabase
from user import User
from bodyparts import BodyParts
@click.command()
def init():
    """Initiate a user and adds it to the database and config file."""
    click.echo("Welcome to")
    click.echo(click.style(r"""
     _______. __  ___  __   __       __       __________   ___    ___       _____    __  
    /       ||  |/  / |  | |  |     |  |     |   ____\  \ /  /    \  \     /  /  |  |  | 
   |   (----`|  '  /  |  | |  |     |  |     |  |__   \  V  /      \  \   /  /|  |__|  | 
    \   \    |    <   |  | |  |     |  |     |   __|   >   <        >  > /  / |   __   | 
.----)   |   |  .  \  |  | |  `----.|  `----.|  |____ /  .  \      /  / /  /  |  |  |  | 
|_______/    |__|\__\ |__| |_______||_______||_______/__/ \__\    /__/ /__/   |__|  |__| 
                                                                                         
               """, fg="red"))
    click.echo("Skillex tracks exercises using commands and tracks your sleep")
    click.echo("Gain xp and level up you and your body")
    click.echo()
    name = click.prompt("Enter in your name")
    user_db = UserDatabase("skillex.db")
    if not user_db.add_user(User(-1, name, 0, BodyParts(), 0, 0)):
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
    
    