import click
from utils.helloWorld import helloWorld
from utils.fetchStock import investment_pull

@click.group()
def cli():
    pass


@cli.command()
def create():
    """
    Create new portfolio
    """
    print('CREATE COMMAND')
    investment_pull(['TWST','FLS','L3H'])


@cli.command()
def add():
    """
    Add asset to specific portfolio
    """
    print('ADD COMMAND')


@cli.command()
def delete():
    """
    Delete asset from specific portfolio
    """
    print('DELETE COMMAND')


@cli.command()
def edit():
    """
    Edit asset in specific portfolio
    """
    print('EDIT COMMAND')


@cli.command()
def summarize():
    """
    Summarize portfolio
    """
    print('SUMMARIZE COMMAND')


@cli.command()
def update():
    """
    Update portfolio with latest stock prices
    """
    print('UPDATE COMMAND')


@cli.command()
def forecast():
    """
    Forecast portfolio
    """
    print('FORECAST COMMAND')


@cli.command()
def plot():
    """
    Command line plot of portfolio performance
    """
    print('PLOT COMMAND')


if __name__ == '__main__':
    cli()