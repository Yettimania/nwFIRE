import pytest


def test_cash(cash_class):
    '''
    Initialize cash asset class.
    '''
    asset = cash_class
    assert(asset.__class__.__name__ == 'Cash')
    assert(asset.amount == 5000)
    asset.summary()


def test_cash_edit(cash_class):
    '''
    Edit cash amount in class object.
    '''
    asset = cash_class
    asset.edit('amount', 1000.50)
    assert(asset.amount == 1000.50)


def test_stock(stock_class):
    '''
    Initialize stock asset class.
    '''
    asset = stock_class
    assert(asset.__class__.__name__ == 'Stock')
    assert(asset.shares == 123.456)
    assert(asset.ticker == 'TWST')
    asset.summary()


def test_equity(equity_class):
    '''
    Initialize equity asset class.

    Edit command is same for the cash so not necessary to repeat.
    '''
    asset = equity_class
    assert(asset.__class__.__name__ == 'Equity')
    assert(asset.amount == 123.45)
    asset.summary()


def test_equity_edit_success(stock_class):
    '''
    Initialize equity asset class.

    Edit command is same for the cash so not necessary to repeat.
    '''
    asset = stock_class
    asset.edit('shares', 500)
    asset.edit('ticker', 'LLL')
    assert(asset.shares == 500)
    assert(asset.ticker == 'LLL')


def test_equity_edit_failure(stock_class):
    '''
    Initialize equity asset class.

    Edit command is same for the cash so not necessary to repeat.
    '''
    asset = stock_class
    asset.edit('shares', 'LLL')


def test_real_estate(realEstate_class):
    '''
    Initialize real estate asset class.

    Edit command is same for the cash so not necessary to repeat.
    '''
    asset = realEstate_class
    assert(asset.__class__.__name__ == 'RealEstate')
    assert(asset.amount == 1200000)
    asset.summary()


def test_fund_class(fund_class):
    '''
    Initialize fund asset class.
    '''
    asset = fund_class
    assert(asset.__class__.__name__ == 'Fund')
    assert(asset.shares == 10.12)
    assert(asset.ticker == 'VWSTX')
    assert(asset.composition == [0.1, 0.4, 0.5])
    assert(asset.composition_type == 'Large Blend')
    asset.summary()
