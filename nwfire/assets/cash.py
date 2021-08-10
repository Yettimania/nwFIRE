from nwfire.assets.asset import Asset


class Cash( Asset ):
    def __init__(self, name, amount):
        self.amount = amount
        self.type = 'CASH'

        Asset.__init__(self, name)
