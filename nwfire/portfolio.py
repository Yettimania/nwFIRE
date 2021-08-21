from os import path
from nwfire.assets.cash import Cash
from nwfire.assets.stock import Stock
from nwfire.assets.equity import Equity
from nwfire.assets.realestate import RealEstate
from nwfire.assets.fund import Fund
from nwfire.utils.operations import fetch_stock_value, percentage


class Portfolio:
    def __init__(self, portfolioName):
        self.name = portfolioName
        self.path = f'./data/{self.name}.pkl'
        self.exist = path.exists(self.path)
        self.assets = {}
        self.networth = 0.00
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
                composition = input(
                    "Enter CASH-BONDS-STOCK Ratio: ").split('-')
                composition = [float(num) for num in composition]
                total = sum(composition)
                if total != 1.0:
                    print('Composition of asset must equal 1.0')
                    exit()
                composition_type = input("Enter category for CASH-BONDS-STOCKS: ").split('-')
                composition_type = [str(x) for x in composition_type]
                if len(composition_type) != 3:
                    print('Must enter a type for CASH, BONDS and STOCKS.')
                    exit()
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
        cash_assets = {}
        stock_assets = {}
        realestate_assets = {}
        fund_assets = {}
        equity_assets = {}

        for name, asset in self.assets.items():
            _asset = asset.__class__.__name__

            if _asset == "Cash":
                cash_assets[name] = asset
            elif _asset == "Stock":
                stock_assets[name] = asset
            elif _asset == "RealEstate":
                realestate_assets[name] = asset
            elif _asset == "Fund":
                fund_assets[name] = asset
            elif _asset == "Equity":
                equity_assets[name] = asset

        print("\nCASH ASSETS")
        print("-" * 26)
        print('{0:8<s}{1:>16s}'.format('NAME', 'VALUE'))
        print("-" * 26)
        for key, asset in cash_assets.items():
            print('{0:<8s} $ {1:>15,.2f}'.format(key, asset.amount))

        print("\nFUND ASSETS")
        print("-" * 26)
        print('{0:8<s}{1:>18s}'.format('NAME', '# SHARES'))
        print("-" * 26)
        for key, asset in fund_assets.items():
            print('{0:<8s} # {1:>15,.3f}'.format(key, asset.shares))

        print("\nSTOCK ASSETS")
        print("-" * 26)
        print('{0:8<s}{1:>18s}'.format('NAME', '# SHARES'))
        print("-" * 26)
        for key, asset in stock_assets.items():
            print('{0:<8s} # {1:>15,.3f}'.format(key, asset.shares))

        print("\nREAL ESTATE ASSETS")
        print("-" * 26)
        print('{0:8<s}{1:>16s}'.format('NAME', 'VALUE'))
        print("-" * 26)
        for key, asset in realestate_assets.items():
            print('{0:<8s} $ {1:>15,.2f}'.format(key, asset.amount))

        print("\nEQUITY ASSETS")
        print("-" * 26)
        print('{0:8<s}{1:>16s}'.format('NAME', 'VALUE'))
        print("-" * 26)
        for key, asset in equity_assets.items():
            print('{0:<8s} $ {1:>15,.2f}'.format(key, asset.amount))
        print()

    def detailed_report(self):
        self._fetch_market_value()

        asset_sums = {
            'Cash': 0.0,
            'Fund': 0.0,
            'Stock': 0.0,
            'RealEstate': 0.0,
            'Equity': 0.0
        }

        asset_types = {
                'Cash':0.00,
                'Stocks':0.00,
                }

        for asset in list(self.assets.values()):
            if asset.__class__.__name__ == 'Fund':
                for comp_type in asset.composition_type:
                    asset_types[comp_type] = 0.00

        for asset in list(self.assets.values()):
            _asset = asset.__class__.__name__

            if _asset == 'Fund':
                _composition = asset.composition
                _composition_type = asset.composition_type
                asset_value = asset.shares * asset.last_closing_price
                for index, comp_value in enumerate(_composition):
                    if comp_value != 0.0:
                        asset_types[_composition_type[index]] += asset_value * comp_value
            elif _asset == 'Stock':
                asset_types['Stocks'] += (asset.shares * asset.last_closing_price)
            elif _asset == 'Cash':
                asset_types['Cash'] += asset.amount


            if _asset == 'Stock' or _asset == 'Fund':
                asset_sums[_asset] += (asset.shares * asset.last_closing_price)
            else:
                asset_sums[_asset] += asset.amount

        self.networth = sum(asset_sums.values())

        print('\nNETWORTH: $ {:,.0f}'.format(self.networth))
        print('-' * 37)
        print('{0:<12s}{1:^15s}{2:>8s}'.format(
               "ASSET", "VALUE", "%"))
        print('-' * 37)

        for asset, value in asset_sums.items():
            print('{0:<12s} $ {1:>10,.0f} {2:>11s}'.format(
            asset, value, percentage(value/self.networth)))
        print()

        print('\nFINANCIAL ALLOCATION')
        print('-' * 37)
        print('{0:<12s}{1:^15s}{2:>8s}'.format(
               "ASSET", "VALUE", "%"))
        print('-' * 37)

        financial_assets = sum(asset_types.values())

        for asset, value in asset_types.items():
            if value != 0.00:
                print('{0:<12s} $ {1:>10,.0f} {2:>11s}'.format(
                asset, value, percentage(value/financial_assets)))


    def _fetch_market_value(self):
        try:
            ticker_list = []

            print("Fetching latest market value...This may take a moment...")

            for key, value in self.assets.items():
                if value.__class__.__name__ == "Stock" or value.__class__.__name__ == "Fund":
                    ticker_list.append(key)

            results = fetch_stock_value(ticker_list)

            for ticker, value in results.items():
                asset = self.assets[ticker]
                asset.last_closing_price = float(value)
            print('Latest market values obtained.')
        except:
            print(f'Unable to fetch stock data on {key}.')
            exit()

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
