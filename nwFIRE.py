import click
from nwfire.portfolio import Portfolio


@click.group()
def cli():
    pass

@cli.command()
def add():
    """
    Add asset to specific portfolio
    """
    print('ADD COMMAND')
    portfolio = Portfolio('KyleLindsay')


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
