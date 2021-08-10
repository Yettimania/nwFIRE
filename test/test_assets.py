import pytest


def test_asset(asset_class):
    asset = asset_class
    assert(asset.name == 'testName')


def test_cash(cash_class):
    asset = cash_class
    assert(asset.name == 'cashName')
    assert(asset.amount == 5000)
    assert(asset.type == 'CASH')


def test_stock(stock_class):
    asset = stock_class
    assert(asset.name == 'stockName')
    assert(asset.shares == 123.456)
    assert(asset.ticker == 'TWST')


def test_equity(equity_class):
    asset = equity_class
    assert(asset.name == 'equityName')
    assert(asset.amount == 123.45)
    assert(asset.type == 'EQUITY')


def test_real_estate(realEstate_class):
    asset = realEstate_class 
    assert(asset.name == 'propName')
    assert(asset.amount == 1200000)
    assert(asset.type == 'REAL_ESTATE')


def test_fund_class(fund_class):
    asset = fund_class
    assert(asset.name == 'fundName')
    assert(asset.shares == 10.12)
    assert(asset.ticker == 'VWSTX')
    assert(asset.composition == [0.1, 0.4, 0.5])
    assert(asset.composition_type == 'Large Blend')
