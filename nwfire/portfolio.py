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
        # TODO
        '''
        If existence is True, load in the assets,
        historical_perf data. If existance False,
        create empty arrays for each.
        '''
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
            asset = Cash(amount)
            self.assets[asset_name] = asset

        elif asset_type.upper() == 'STOCK':
            # TODO
            print('You are adding stock.')
        elif asset_type.upper() == 'REALESTATE':
            # TODO
            print('You are adding real estate.')
        elif asset_type.upper() == 'EQUITY':
            # TODO
            print('You are adding equity.')
        elif asset_type.upper() == 'FUND':
            # TODO
            print('You are adding fund.')
        # TODO Prompt based on asset_type
        # TODO Add asset which was passed in
        # TODO Write portfolio to record again

    def delete_asset(self):
        print("Deleting asset.")

    def edit_asset(self):
        None

    def forecast_portfolio(self):
        None

    def plot_performance(self):
        None

    def summarize_portfolio(self):
        None

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
