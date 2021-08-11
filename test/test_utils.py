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
    Test the loading of a portfolio from a picle file to
    conduct additional operations.
    '''
    portfolio = load_portfolio('./test/test_portfolio.pkl')
    assert(bool(portfolio.assets))
    assert(portfolio.assets['TEST'].__class__.__name__ == 'Cash')
    assert(portfolio.assets['TEST'].amount == 100.12)

