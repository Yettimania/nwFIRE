class Equity():
    def __init__(self, amount):
        self.amount = amount

    def edit(self, field, value):
        try:
            self.amount = float(value)
        except:
            print('Unable to edit cash asset to specific value.')
