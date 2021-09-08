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
def summary(ctx, asset):
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
            portfolio.summarize_portfolio()


@cli.command()
@click.pass_context
def report(ctx):
    """
    Update portfolio with latest stock prices
    """
    portfolio_name = ctx.obj['PORTFOLIO']
    pkl_path = f'./data/{portfolio_name}.pkl'
    if path.exists(pkl_path):
        portfolio = load_portfolio(pkl_path)
        portfolio.detailed_report()
        save_portfolio(portfolio)
    else:
        print("Portfolio not found. Exiting program.")


@cli.command()
@click.pass_context
def append_history(ctx):
    """
    Append historical data to a portfolio
    """
    portfolio_name = ctx.obj['PORTFOLIO']
    pkl_path = f'./data/{portfolio_name}.pkl'
    if path.exists(pkl_path):
        try:
            portfolio = load_portfolio(pkl_path)
            date = str(input("Enter date of evaluation (MM/DD/YY): "))
            networth = float(input("Enter networth on date: "))
            financial_value = float(input("Enter financial value on date: "))
            portfolio.append_history(date, networth, financial_value)
            print(portfolio.historical_perf)
            save_portfolio(portfolio)
        except:
            print("Could not append historical data.")
            print("Confirm date format and float value entered.")
    else:
        print("Portfolio not found. Exiting program.")

@cli.command()
@click.pass_context
def delete_history(ctx):
    """
    Delete a date value pair from class object.
    """
    portfolio_name = ctx.obj['PORTFOLIO']
    pkl_path = f'./data/{portfolio_name}.pkl'
    if path.exists(pkl_path):
        try:
            portfolio = load_portfolio(pkl_path)
            print("List of dates in history...")
            print(list(portfolio.historical_perf.keys()))
            response = input("Enter date you'd like to delete: ")
            portfolio.historical_perf.pop(str(response))
            save_portfolio(portfolio)
        except:
            print("Could not delete date for historical data.")
            print("Confirm date format is correct. ")

@cli.command()
def forecast():
    """
    Forecast portfolio
    """
    print('FORECAST COMMAND')


if __name__ == '__main__':
    cli(obj={})
