import pytest
from nwfire.utils.operations import *


def test_portfolio_name(portolio_class):
    '''
    Verify name of portfolio as its created.
    '''
    portfolio = portolio_class
    assert(portfolio.name == 'testPortfolio')

def test_portfolio_path(portolio_class):
    '''
    Correctly establish path to data file location.
    '''
    portfolio = portolio_class
    assert(portfolio.path == './data/testPortfolio.pkl')

def test_portfolio_not_exist(portolio_class):
    '''
    Testing to determine if a pickle file exists for the
    portfolio. If not, it will use the prompt when calling
    the ADD command. Other commands with return an error
    because the operations can be performed on a portfolio
    that does not exist.
    '''
    portfolio = portolio_class
    assert(portfolio.exist == False)

def test_portfolio_add(testPortfolio):
    # SET TO TRUE FOR TEST ONLY
    testPortfolio.add_asset('cash')
    print(testPortfolio.assets)

def test_portfolio_delete(testPortfolio):
   testPortfolio.delete_asset('CASH')
   result = 'CASH' in testPortfolio.assets
   assert(result == False)
