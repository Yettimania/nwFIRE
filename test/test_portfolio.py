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

def test_portfolio_delete(testPortfolio):
   testPortfolio.delete_asset('CASH')
   result = 'CASH' in testPortfolio.assets
   assert(result == False)

def test_portfolio_edit(testPortfolio):
    testPortfolio.edit_asset('CASH', 'amount', 2000.50)
    result = testPortfolio.assets['CASH'].amount
    assert(result == 2000.50)

    testPortfolio.edit_asset('EQUITY', 'amount', 123.50)
    result = testPortfolio.assets['EQUITY'].amount
    assert(result == 123.50)

    testPortfolio.edit_asset('REALESTATE', 'amount', 1235000)
    result = testPortfolio.assets['REALESTATE'].amount
    assert(result == 1235000)

    testPortfolio.edit_asset('STOCK', 'shares', 500)
    result = testPortfolio.assets['STOCK'].shares
    assert(result == 500)

    testPortfolio.edit_asset('FUND', 'composition', "0.2-0.5-0.3")
    result = testPortfolio.assets['FUND'].composition
    assert(result == [0.2,0.5,0.3])

    testPortfolio.edit_asset('FUND', 'composition_type', 'SMALL_CAP')
    result = testPortfolio.assets['FUND'].composition_type
    assert(result == ['SMALL_CAP'])

def test_portfolio_append_history(testPortfolio):
    testPortfolio.append_history('09/08/21', 1000.12)
    result = testPortfolio.historical_perf['09/08/21']
    print(testPortfolio.historical_perf)
    assert (result == 1000.12)
