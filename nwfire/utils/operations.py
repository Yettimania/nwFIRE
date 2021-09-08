import pickle
from yahoofinancials import YahooFinancials
from multiprocessing import Process
from asciichartpy import plot
from datetime import datetime
import numpy as np
import pandas as pd

result = {}

def save_portfolio(portfolio):
    file = open(portfolio.path, 'wb')
    pickle.dump(portfolio, file)
    file.close()


def load_portfolio(portfolio_path):
    file = open(portfolio_path, 'rb')
    portfolio = pickle.load(file)
    file.close()
    portfolio.exist = True
    return portfolio


def percentage(value):
    percentage = f'{value * 100:.1f} %'
    return percentage


def fetch_stock_value(invest_list):

    def get_prices(tickers):
        global result

        for ticker in tickers:
            tickerdata = YahooFinancials(ticker)
            prevclose = tickerdata.get_prev_close_price()
            result[ticker] = prevclose
        return (result)

    tickers = invest_list

    p1 = Process(target=get_prices, args=(tickers,))
    p1.start()
    p1.join()

    return get_prices(tickers)

''' NOTE THIS MAY NOT WORK DUE TO SCALING '''
def plot_history(history_dict):
    hist_datetime = [datetime.strptime(i, '%m/%d/%y') for i in history_dict.keys()]
    delta_days = [0]
    for index in range(len(hist_datetime)-1):
        delta_days.append((hist_datetime[index+1] - hist_datetime[0]).days)

    nw_values = list(history_dict.values())
    nw_values_normalized = [value/100000 for value in nw_values]

    series = [nw_values_normalized[0]]
    for index in range(1,len(delta_days)):
        series.extend(np.linspace(nw_values_normalized[index-1],nw_values_normalized[index],(delta_days[index]-delta_days[index-1])))

    rolling_series = pd.Series(series).rolling(800).max().dropna().tolist()

    print("PORTFOLIO PERFORMANCE ($100,000)")
    print(plot(rolling_series, {'height': 20,
                        'offset': 2,
                        'format': '${:8,.1f}',
                        'colors': ['\x1b[32m'],
                        'min': min(nw_values_normalized),
                        'max': max(nw_values_normalized)}))
