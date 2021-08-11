import pytest
from nwfire.assets.cash import Cash
from nwfire.assets.stock import Stock
from nwfire.assets.equity import Equity
from nwfire.assets.realestate import RealEstate
from nwfire.assets.fund import Fund
from nwfire.portfolio import Portfolio

@pytest.fixture
def testPortfolio():
    print("FOR TESTING USE NAME 'TEST' with value '100.12'")
    portfolio = Portfolio('test_portfolio')
    # SET PATH MANUALLY FOR TEST ONLY
    portfolio.path = './test/test_portfolio.pkl'
    portfolio.add_asset('cash')
    return portfolio


@pytest.fixture
def portolio_class():
    return Portfolio('testPortfolio')


@pytest.fixture
def cash_class():
    return Cash(5000)


@pytest.fixture
def stock_class():
    return Stock(123.456, 'TWST')


@pytest.fixture
def equity_class():
    return Equity(123.45)


@pytest.fixture
def realEstate_class():
    return RealEstate(1200000)

@pytest.fixture
def fund_class():
    return Fund(10.12, 'VWSTX',
            [0.1,0.4,0.5], 'Large Blend')
