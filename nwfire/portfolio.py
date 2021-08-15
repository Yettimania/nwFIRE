from os import path
from nwfire.assets.cash import Cash
from nwfire.assets.stock import Stock
from nwfire.assets.equity import Equity
from nwfire.assets.realestate import RealEstate
from nwfire.assets.fund import Fund


class Portfolio:
    def __init__(self, portfolioName):
        self.name = portfolioName
        self.path = f'./data/{self.name}.pkl'
        self.exist = path.exists(self.path)
        self.assets = {}
        self.historical_perf = []

    def add_asset(self, asset_type):
        self._prompt_existence()
        if asset_type.upper() == 'CASH':
            print('Adding cash asset to portfolio...')
            asset_name = str(input("Name of asset: ")).upper()
            try:
                amount = float(input("Cash value of asset: "))
            except ValueError:
                print('Amount must be an integer or float.')
                exit()
            self.assets[asset_name] = Cash(amount)
        elif asset_type.upper() == 'STOCK':
            print('Adding stock asset to portfolio...')
            try:
                ticker = str(input("Ticker Symbol: ")).upper()
                num_shares = float(input("Number of Shares: "))
            except ValueError:
                print('Amount must be integer or float.')
            self.assets[ticker] = Stock(num_shares, ticker)
        elif asset_type.upper() == 'REALESTATE':
            print('Adding real estate to portfolio...')
            try:
                name = str(input("Name of property: ")).upper()
                amount = float(input("Property Equity Value: "))
            except ValueError:
                print('Amount must be an integer or float.')
                exit()
            self.assets[name] = RealEstate(amount)
        elif asset_type.upper() == 'EQUITY':
            print('Adding equity stakes to portfolio...')
            try:
                name = str(input("Name of Equity: ")).upper()
                amount = float(input("Equity Value: "))
            except ValueError:
                print('Amount must be an integer or float.')
                exit()
            self.assets[name] = Equity(amount)
        elif asset_type.upper() == 'FUND':
            print('Adding funds to portfolio...')
            try:
                name = str(input("Funds Ticker: ")).upper()
                num_shares = float(input("Number of Shares: "))
                composition = input("Enter [CASH,BONDS,STOCK] Ratio: ").split(' ')
                composition = [float(num) for num in composition]
                total = sum(composition)
                if total != 1.0:
                    print('Composition of asset must equal 1.0')
                    exit()
                composition_type = str(input("Enter fund category: "))
            except ValueError:
                print('Value Error: Amount must be an integer or float. \
                        composition must be ratios that add to 1.')
                exit()
            self.assets[name] = Fund(num_shares, name,
                    composition, composition_type)
        else:
            print('Asset type not recognized. Please select \
                    CASH, STOCK, EQUITY, REALESTATE, FUND.')
        print('Asset has been added to portfolio.')

    def delete_asset(self, asset_key):
        print("Deleting asset from portfolio...")
        try:
            del self.assets[asset_key]
        except:
            print('Unable to delete asset from portoflio.')
            print('Confirm argument passed in is correct.')


    def edit_asset(self, asset_key, field, value):
        print(f'Editing asset {asset_key} in portfolio...')
        try:
            asset_class = self.assets[asset_key]
        except:
            print('Unable to located asset in portfolio.')
            exit()

        asset_class.edit(field, value)


    def forecast_portfolio(self):
        None

    def plot_performance(self):
        None

    def summarize_portfolio(self):
        print("Summary of portfolio")

    def update_market_value(self):
        None

    def _prompt_existence(self):
        if self.exist == False:
            response = input('Portfolio does not exist.'
                             ' Would you like to create {} [y/n]? '
                             .format(self.name))
            if response == 'y':
                pass
            elif response == 'n':
                print('Portfolio not created.')
                exit()
            else:
                print('Response note recognized. Exiting program.')
