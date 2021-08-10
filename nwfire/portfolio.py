import nwfire.assets
from os import path

class Portfolio:
    def __init__(self, portfolioName):
        self.name = portfolioName
        self.path = f'/data/{self.name}.pkl'
        self.exist = path.exists(self.path)
        if self.exist == False:
            response = input('Portfolio does not exist.'
                    ' Would you like to create {} [y/n]? '
                    .format(self.name))
            if response == 'y':
                pass
            elif response == 'n':
                print('Portfolio not created.')
                exit
            else:
                print('Response note recognized. Exiting program.')

    def add_asset(self):
        None

    def delete_asset(self):
        None

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
