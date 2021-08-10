from nwfire.assets.asset import Asset


class Stock( Asset ):
    def __init__(self, name, shares, ticker):
        self.shares = shares
        self.ticker = ticker
        self.last_closing_price = None
        self.type = 'STOCK'

        Asset.__init__(self, name)
