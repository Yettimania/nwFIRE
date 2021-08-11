import pytest


def test_cash(cash_class):
    asset = cash_class
    assert(asset.__class__.__name__ == 'Cash')
    assert(asset.amount == 5000)


def test_stock(stock_class):
    asset = stock_class
    assert(asset.__class__.__name__ == 'Stock')
    assert(asset.shares == 123.456)
    assert(asset.ticker == 'TWST')


def test_equity(equity_class):
    asset = equity_class
    assert(asset.__class__.__name__ == 'Equity')
    assert(asset.amount == 123.45)


def test_real_estate(realEstate_class):
    asset = realEstate_class 
    assert(asset.__class__.__name__ == 'RealEstate')
    assert(asset.amount == 1200000)


def test_fund_class(fund_class):
    asset = fund_class
    assert(asset.__class__.__name__ == 'Fund')
    assert(asset.shares == 10.12)
    assert(asset.ticker == 'VWSTX')
    assert(asset.composition == [0.1, 0.4, 0.5])
    assert(asset.composition_type == 'Large Blend')
