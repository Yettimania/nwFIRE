import yfinance as yf

class Asset:

    def __init__(self,name,load=False):
        if load:
            self.name = None
            self.category = None
            self.detail = None
            self.amount = None
            self.composition = None
            self.ticker = None
        else:
            self.name = name
            self.category = self._category_prompt()
            self.detail = self._morningstar_grid()
            self.amount = self._get_amount()
            self.composition = self._get_composition()
            self.ticker = self._get_ticker()

    def edit(self):
        if self.category == "Investment":
            menu = {}
            menu['1'] = "Category"
            menu['2'] = "Amount"
            menu['3'] = "Composition"
            menu['4'] = "Ticker"
        else:
            menu = {}
            menu['1'] = "Amount"
    
        options = menu.keys()
        print("Select category of edit:")
        for entry in options:
            print(entry,menu[entry])

        selection = input(f'>> ')

        choice = menu[selection]

        if choice == "Category":
            self.category = self._category_prompt()
        if choice == "Amount":
            self.amount = self._get_amount()
        if choice == "Composition":
            self.composition = self._get_composition()
        if choice == "Ticker":
            self.ticker = self._get_ticker()

    def _category_prompt(self):
        menu = {}
        menu['1'] = "Cash"
        menu['2'] = "Investment"
        menu['3'] = "Real Estate"
        menu['4'] = "Owner Equity"

        options = menu.keys()
        print("Select category of asset:")
        for entry in options:
            print(entry,menu[entry])
        
        selection = input(f'>> ')

        return menu[selection]

    def _get_amount(self):
        if self.category == 'Investment':
            amount = float(input('Enter shares owned of asset: '))
        else:
            amount = float(input('Enter dollar amount of asset: '))
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
            print("Select Mornging Star Category:")
            for entry in options:
                print(entry,menu[entry])
            
            selection = input(">> ")

            return menu[selection] 
        else:
            return None

    def _get_ticker(self):
        if self.category == 'Investment':
            ticker = input("Enter asset ticker: ")
            return ticker
        else:
            return None

    def _get_composition(self):
        if self.category == 'Investment':
            cash = float(input("Enter cash composition: "))
            bonds = float(input("Enter bond composition: "))
            stocks = float(input("Enter stock composition: "))
            return [cash,bonds,stocks]
        else:
            return None
    
    @property
    def value(self):
        return self._get_value()

    def _get_value(self):
        if self.category == 'Investment':
            value = self.amount
        else:
            tickerdata = yf.Ticker(self.ticker)
            prevclose = tickerdata.info['previousClose']
            value = self.amount* prevclose
        return float(value)
