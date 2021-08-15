import pickle


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
