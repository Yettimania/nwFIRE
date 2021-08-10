from nwfire.assets.asset import Asset


class Fund(Asset):
    def __init__(self, name, shares, ticker,
                 composition, composition_type):
        self.shares = shares
        self.ticker = ticker
        self.composition = composition
        self.composition_type = composition_type
        self.type = 'FUND'

        Asset.__init__(self, name)
