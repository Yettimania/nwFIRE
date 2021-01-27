def asset_dict():
     asset_dict = { 'Cash':0.0,
                    'Bonds':0.0,
                    'Stocks':0.0,
                    'RealEstate':0.0,
                    'Equity':0.0 }

     return asset_dict

def detailed_dict():
    detailed_dict = {'Cash':0.0,
                     'Short Bonds':0.0,
                     'Medium Bonds':0.0,
                     'Long Bonds':0.0,
                     'Large Value': 0.0,
                     'Large Blend': 0.0,
                     'Large Growth': 0.0,
                     'Mid Cap': 0.0,
                     'Small Cap': 0.0,
                     'Stocks':0.0 }
    return detailed_dict

def networth(assets):
    networth = sum(assets.values())

    dash = '-' * 37
    print('\nTOTAL NETWORTH BREAKDOWN')
    print(dash)
    print('{:<10s}{:>11s}{:>16s}'.format('ASSET','VALUE','PERCENTAGE'))
    print(dash)
    
    for key,value in assets.items():
        print('{:<15s}$ {:>8.2f}{:>10.2%}'.format(key,value,value/networth))

    print(dash)
    print('{:<15s}${:>9.2f}\n'.format('NETWORTH',networth))
    
def financial_breakdown(assets):
    total_financial = sum(assets.values())
    total_cash = assets['Cash']
    total_bonds = assets['Long Bonds'] + assets['Medium Bonds'] + assets['Short Bonds']
    total_stocks = assets['Large Value'] + \
                   assets['Large Blend'] + \
                   assets['Large Growth'] + \
                   assets['Mid Cap'] + \
                   assets['Small Cap'] + \
                   assets['Stocks']

    dash = '-' * 53 
    names = list(assets.keys())

    print("DETAILED FINANCIAL BREAKDOWN")
    # PRINT CASH ASSETS
    print(dash)
    print('{:<10s}{:>14s}{:>15s}{:>10s}'.format('ASSET','VALUE','% CLASS','% TOTAL'))
    print(dash)
    print_asset(names[0],total_cash,total_cash/total_cash,total_cash/total_financial)
    print(dash)
    print_asset('TOTAL CASH',total_cash,total_cash/total_cash,total_cash/total_financial)
    print(dash + '\n')

    # PRINT BOND ASSETS
    print_asset(names[1],assets['Short Bonds'],assets['Short Bonds']/total_bonds,assets['Short Bonds']/total_financial)
    print_asset(names[2],assets['Medium Bonds'],assets['Medium Bonds']/total_bonds,assets['Medium Bonds']/total_financial)
    print_asset(names[3],assets['Long Bonds'],assets['Long Bonds']/total_bonds,assets['Long Bonds']/total_financial)
    print(dash)
    print_asset('TOTAL BONDS',total_bonds,total_bonds/total_bonds,total_bonds/total_financial)
    print(dash + '\n')

    # PRINT STOCK DETAILS
    print_asset(names[4],assets['Large Value'],assets['Large Value']/total_stocks,assets['Large Value']/total_financial)
    print_asset(names[5],assets['Large Blend'],assets['Large Blend']/total_stocks,assets['Large Blend']/total_financial)
    print_asset(names[6],assets['Large Growth'],assets['Large Growth']/total_stocks,assets['Large Growth']/total_financial)
    print_asset(names[7],assets['Mid Cap'],assets['Mid Cap']/total_stocks,assets['Mid Cap']/total_financial)
    print_asset(names[8],assets['Small Cap'],assets['Small Cap']/total_stocks,assets['Small Cap']/total_financial)
    print_asset(names[9],assets['Stocks'],assets['Stocks']/total_stocks,assets['Stocks']/total_financial)
    print(dash)
    print_asset('TOTAL STOCKS',total_stocks,total_stocks/total_stocks,total_stocks/total_financial)
    print(dash)

    # TOTAL FINANCIAL ASSETS
    print('{:<16s}{:>10s}{:>10.2f}'.format('TOTAL FINANCIAL ASSETS','$',total_financial))
    print('\n')

def print_asset(name,value,class_percent,total_percent):
    print('{:<16s}${:>8.2f}{:>14.2%}{:>10.2%}'.format(name,value,class_percent,total_percent))


