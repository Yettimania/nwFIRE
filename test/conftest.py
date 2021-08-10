import pytest
from nwfire.assets.asset import Asset
from nwfire.assets.cash import Cash
from nwfire.assets.stock import Stock
from nwfire.assets.equity import Equity
from nwfire.assets.realEstate import RealEstate
from nwfire.assets.fund import Fund
from nwfire.portfolio import Portfolio


@pytest.fixture
def portolio_class():
    return Portfolio('testPortfolio')

@pytest.fixture
def asset_class():
    return Asset('testName')


@pytest.fixture
def cash_class():
    return Cash('cashName', 5000)


@pytest.fixture
def stock_class():
    return Stock('stockName', 123.456, 'TWST')


@pytest.fixture
def equity_class():
    return Equity('equityName', 123.45)


@pytest.fixture
def realEstate_class():
    return RealEstate('propName', 1200000)

@pytest.fixture
def fund_class():
    return Fund('fundName', 10.12, 'VWSTX',
            [0.1,0.4,0.5], 'Large Blend')
