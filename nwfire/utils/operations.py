import pickle
from yahoofinancials import YahooFinancials
from multiprocessing import Process

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
