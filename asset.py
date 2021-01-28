import yfinance as yf

class Asset:

    def __init__(self,name,load=False):
        if load:
            self.name = None
            self.category = None
            self.retirement = False
            self.amount = None
            self.composition = None
            self.comp_type = None
            self.ticker = None
        else:
            self.name = name
            self.category = self._category_prompt()
            self.retirement = self._get_retirement()
            self.amount = self._get_amount()
            self.composition = None 
            self.comp_type = None 
            self._get_composition()
            self.ticker = self._get_ticker()

    def edit(self):
        if self.category == "Investment":
            menu = {}
            menu['1'] = "Category"
            menu['2'] = "Amount"
            menu['3'] = "Composition"
            menu['4'] = "Ticker"
            menu['5'] = "Retirement"
        else:
            menu = {}
            menu['1'] = "Amount"
    
        options = menu.keys()
        print("EDIT ATTRIBUTE")
        for entry in options:
            print(entry,menu[entry])

        selection = input('Select Attribute to Edit: ')

        choice = menu[selection]

        if choice == "Category":
            self.category = self._category_prompt()
        if choice == "Amount":
            self.amount = self._get_amount()
        if choice == "Composition":
            self.composition = self._get_composition()
        if choice == "Ticker":
            self.ticker = self._get_ticker()
        if choice == "Retirement":
            self.retirement = self._get_retirement()

    def _category_prompt(self):
        menu = {}
        menu['1'] = "Cash"
        menu['2'] = "Investment"
        menu['3'] = "Real Estate"
        menu['4'] = "Owner Equity"

        options = menu.keys()
        print("ASSET CATEGORIES")
        for entry in options:
            print(entry,menu[entry])
        
        while True:
            selection = input("Select Asset Category: ")
            if selection in menu.keys():
                break 
            else:
                print('Select option in the menu.')
                continue

        return menu[selection]

    def _get_amount(self):
        if self.category == 'Investment':
            while True:
                try:
                    amount = float(input('Enter qty of shares: '))
                except ValueError:
                    print("Needs to be numeric value...")
                else:
                    break
        else:
            while True:
                try:
                    amount = float(input('Enter $ value of asset: '))
                except ValueError:
                    print("Needs to be numeric value...")
                else:
                    break
        return amount

    def _morningstar_grid(self):
        if self.category == 'Investment':
            menu = {}
            menu['1'] = 'Cash'
            menu['2'] = 'Short Bonds'
            menu['3'] = 'Medium Bonds'
            menu['4'] = 'Long Bonds'
            menu['5'] = 'Large Blend'
            menu['6'] = 'Large Growth'
            menu['7'] = 'Large Value'
            menu['8'] = 'Mid Cap'
            menu['9'] = 'Small Cap'
            menu['10'] = 'Ind Stock'
            menu['11'] = 'Blend'
           
            options = menu.keys()
            print("MORNING STAR CATEGORIES")
            for entry in options:
                print(entry,menu[entry])

            while True:
                selection = input("Select Morning Star Category: ")
                if selection in menu.keys():
                    break 
                else:
                    print('Select option in the menu.')
                    continue

            return menu[selection] 
        else:
            return None

    def _get_ticker(self):
        if self.category == 'Investment':
            ticker = input("Enter asset ticker: ").upper()
            return ticker
        else:
            return None

    def _get_composition(self):
        if self.category == 'Investment':
            while True:
                try:
                    cash = float(input('Enter cash fraction [0-1]: '))
                except ValueError:
                    print("Needs to be numeric value...")
                else:
                    break
            cash_type = 'Cash'
            while True:
                try:
                    bonds = float(input('Enter bonds fraction [0-1]: '))
                except ValueError:
                    print("Needs to be numeric value...")
                else:
                    break
            bond_type = self._morningstar_grid()
            while True:
                try:
                    stocks = float(input('Enter stocks fraction [0-1]: '))
                except ValueError:
                    print("Needs to be numeric value...")
                else:
                    break
            stock_type = self._morningstar_grid()
            self.composition = [cash,bonds,stocks]
            self.comp_type = [cash_type,bond_type,stock_type]
        else:
            return None

    def _get_retirement(self):
        value = input("Is this a retirement fund (y/n): ")
        if value == 'y':
            return True
        else:
            return False
    
    @property
    def value(self):
        if self.category == 'Investment':
            return self._get_value()
        else:
            return self.amount

    def _get_value(self):
        if self.category == 'Investment':
            value = self.amount
        else:
            tickerdata = yf.Ticker(self.ticker)
            prevclose = tickerdata.info['previousClose']
            value = self.amount* prevclose
        return float(value)
