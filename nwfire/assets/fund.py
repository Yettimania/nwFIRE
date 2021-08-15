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
