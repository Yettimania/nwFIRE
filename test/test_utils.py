from utils.fetchStock import investment_pull


def test_investment_pull():
    stockList = ['FLS', 'TWST', 'VWSTX']
    investment_pull(stockList)
