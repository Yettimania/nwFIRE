from nwfire.assets.asset import Asset


class RealEstate( Asset ):
    def __init__(self, name, amount):
        self.amount = amount
        self.type = 'REAL_ESTATE'

        Asset.__init__(self, name)
