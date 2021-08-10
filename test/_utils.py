from nwfire.utils.fetchStock import investment_pull


def test_investment_pull():
    stockList = ['FLS', 'TWST', 'VWSTX']
    response = investment_pull(stockList)
    print(response)
