import click
from bodyparts import BodypartList
@click.command()
def bodyparts() -> None:
    """Echoes all available bodyparts"""
    bodypartList = BodypartList()
    sortedBodyparts = sorted(bodypartList.bodyparts)
    click.echo("Available bodyparts:")
    for i in range(len(sortedBodyparts)):
        click.echo(f"   {sortedBodyparts[i]}")