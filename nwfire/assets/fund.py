from nwfire.utils.operations import percentage


class Fund():
    def __init__(self, shares, ticker,
                 composition, composition_type):
        self.shares = shares
        self.ticker = ticker
        self.composition = composition
        self.composition_type = composition_type

    def edit(self, field, value):
        try:
            if field.upper() == "SHARES":
                self.shares = float(value)
            elif field.upper() == "TICKER":
                self.ticker = str(value)
            elif field.upper() == "COMPOSITION":
                self.composition = list(value)
            elif field.upper() == "COMPOSITION_TYPE":
                self.composition_type = str(value)
            else:
                print("Specific field no found or unable to edit.")
        except ValueError:
            print("Cant cast specifc value.")


    def summary(self):
        print(f'Shares: {self.shares}')
        print(f'Ticker: {self.ticker}')
        print(f'Cash Percentage: {percentage(self.composition[0])}')
        print(f'Bond Percentage: {percentage(self.composition[1])}')
        print(f'Stock Percentage: {percentage(self.composition[2])}')
        print(f'Composition Type: {self.composition_type}')
