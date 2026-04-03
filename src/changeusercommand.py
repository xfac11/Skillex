import click
from config import save_config
from userdatabase import UserDatabase

@click.command()
@click.argument("name", type=str)
def change(name:str):
    """Change the current user to the user with this name"""
    user_db = UserDatabase()
    if not user_db.exists():
        click.echo("No user database exists. Call init first to create a user")
        return
    user = user_db.get_user(name)
    if not user:
        click.echo("No user with that name exists")
        return
    save_config(user.name, user.id)
    click.echo(f"Changed the current user to {click.style(user.name, fg="yellow")}")