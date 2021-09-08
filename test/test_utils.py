import pytest
from nwfire.portfolio import Portfolio
from nwfire.utils.operations import *


def test_portfolio_save(testPortfolio):
    '''
    Test saving a portfolio object to a pickle file
    '''
    save_portfolio(testPortfolio)
    assert True

def test_portfolio_load():
    '''
    Test the loading of a portfolio from a pickle file to
    conduct additional operations.
    '''
    portfolio = load_portfolio('./test/test_portfolio.pkl')
    print(f'PORTFOLIO ASSETS: {portfolio.assets}')
    assert(bool(portfolio.assets))
    assert(portfolio.assets['CASH'].__class__.__name__ == 'Cash')
    assert(portfolio.assets['CASH'].amount == 5000)

def test_fetch_stock_value():
    invest_list = ["TWST", "L3H", "FLS", "XIX"]
    result = fetch_stock_value(invest_list)
    print(result)
    assert True


def test_plot_history():
    history = {
            '01/04/19': 10000,
            '11/22/19': 50000.12,
            '03/14/20': 500000.143,
            '09/08/21': 750000
            }
    plot_history(history)
