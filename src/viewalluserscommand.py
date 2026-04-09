import click
from userdatabase import UserDatabase

@click.command()
def users():
    user_db = UserDatabase()
    if not user_db.exists():
        click.echo("No users. Add users with skillex init")
        return
    users = user_db.get_all()
    if len(users) == 0:
        click.echo("No users. Add users with skillex init")
    
    click.echo("Showing all users")
    click.echo("---------")
    for user in users:
        click.echo(user.name)
    