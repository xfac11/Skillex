import click
from searchcommand import search
from bodypartscommand import bodyparts
from viewusercommand import stats
from addexercisecommand import add
from addsleepcommand import sleep
from initcommand import init
from logcommand import log
from viewexercisecommand import view
from changeusercommand import change
@click.group()
def cli() -> None:
    """An exercise tracker CLI using gamification"""
    pass
        
cli.add_command(search)
cli.add_command(bodyparts)
cli.add_command(stats)
cli.add_command(sleep)
cli.add_command(add)
cli.add_command(init)
cli.add_command(log)
cli.add_command(view)
cli.add_command(change)

if __name__ == "__main__":
    cli()
