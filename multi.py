from yahoofinancials import YahooFinancials
from multiprocessing import Process

result = {}
    
def investment_pull(invest_list):

    def get_prices(tickers):
        global result
        
        for ticker in tickers:
            tickerdata = YahooFinancials(ticker)
            prevclose = tickerdata.get_prev_close_price()
            result[ticker] = prevclose
        return (result)
    
    tickers = invest_list 

    p1 = Process(target=get_prices,args=(tickers,))
    p1.start()
    p1.join()

    return get_prices(tickers)

