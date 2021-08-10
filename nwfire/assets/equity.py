from nwfire.assets.asset import Asset


class Equity( Asset ):
    def __init__(self, name, amount):
        self.amount = amount
        self.type = 'EQUITY'

        Asset.__init__(self, name)
