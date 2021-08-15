import click
from os import path
from nwfire.portfolio import Portfolio
from nwfire.utils.operations import save_portfolio, load_portfolio


@click.group()
@click.option('--portfolio', required=True, type=str)
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
    portfolio_name = ctx.obj['PORTFOLIO']
    pkl_path = f'./data/{portfolio_name}.pkl'
    if path.exists(pkl_path):
        portfolio = load_portfolio(pkl_path)
    else:
        portfolio = Portfolio(portfolio_name)

    portfolio.add_asset(asset_type)
    save_portfolio(portfolio)


@cli.command()
@click.pass_context
@click.argument('asset_key')
def delete(ctx, asset_key):
    """
    Delete asset from specific portfolio
    """
    portfolio_name = ctx.obj['PORTFOLIO']
    pkl_path = f'./data/{portfolio_name}.pkl'
    if path.exists(pkl_path):
        portfolio = load_portfolio(pkl_path)
        portfolio.delete_asset(asset_key)
        save_portfolio(portfolio)
    else:
        print("Portfolio does not exist. Can't delete.")


@cli.command()
@click.pass_context
@click.argument('asset_key')
@click.option('--field', required=True, type=str)
@click.option('--value', required=True, type=str)
def edit(ctx, asset_key, field, value):
    """
    Edit asset in specific portfolio
    """
    portfolio_name = ctx.obj['PORTFOLIO']
    pkl_path = f'./data/{portfolio_name}.pkl'
    if path.exists(pkl_path):
        portfolio = load_portfolio(pkl_path)
        portfolio.edit_asset(asset_key, field, value)
        save_portfolio(portfolio)
    else:
        print("Portfolio does not exist. Can't delete.")


@cli.command()
@click.pass_context
@click.option('--asset', type=str)
def summarize(ctx, asset):
    """
    Summarize portfolio
    """
    portfolio_name = ctx.obj['PORTFOLIO']
    pkl_path = f'./data/{portfolio_name}.pkl'
    if path.exists(pkl_path):
        portfolio = load_portfolio(pkl_path)
        if bool(asset):
            if asset in portfolio.assets.keys():
                print(f'Portfolio Asset: {asset.upper()}')
                portfolio.assets[asset.upper()].summary()
            else:
                print("Asset not found in portfolio.")
        else:
            print("Portfolio Only!")
            print(portfolio.assets)
            portfolio.summarize_portfolio()


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
