import click
from nwfire.portfolio import Portfolio
from nwfire.utils.operations import save_portfolio 


@click.group()
@click.option('--portfolio', required = True, type = str)
@click.pass_context
def cli(ctx, portfolio):
    ctx.ensure_object(dict)
    ctx.obj['PORTFOLIO'] = portfolio

@cli.command()
@click.pass_context
@click.argument('asset_type')
def add(ctx, asset_type):
    """
    Add asset to specific portfolio
    """
    portfolio = Portfolio(ctx.obj['PORTFOLIO'])
    portfolio.add_asset(asset_type)
    save_portfolio(portfolio)


@cli.command()
def delete():
    """
    Delete asset from specific portfolio
    """
    print('DELETE COMMAND')
    if not portfolio.exist:
        print("Portfolio does not exist. Can't delete.")


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
    cli(obj={})
