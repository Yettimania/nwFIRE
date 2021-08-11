class Fund():
    def __init__(self, shares, ticker,
                 composition, composition_type):
        self.shares = shares
        self.ticker = ticker
        self.composition = composition
        self.composition_type = composition_type
