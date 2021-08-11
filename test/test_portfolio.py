import pytest


def test_portfolio_name(portolio_class):
    portfolio = portolio_class
    assert(portfolio.name == 'testPortfolio')

def test_portfolio_path(portolio_class):
    portfolio = portolio_class
    assert(portfolio.path == './data/testPortfolio.pkl')

def test_portfolio_not_exist(portolio_class):
    portfolio = portolio_class
    assert(portfolio.exist == False)
