class Stock():
    def __init__(self, shares, ticker):
        self.shares = shares
        self.ticker = ticker
        self.last_closing_price = None

    def edit(self, field, value):
        try:
            if field.upper() == 'SHARES':
                self.shares = float(value)
            elif field.upper() == 'TICKER':
                self.ticker = str(value)
            else:
                print("Specify field not found or unable to edit.")
        except ValueError:
            print("Can't cast shares to float value.")
