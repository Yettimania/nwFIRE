import numpy as np
from os import path
import matplotlib.pyplot as plt
import yaml
from datetime import date

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

    dash = '-' * 67
    print('\nTOTAL NETWORTH BREAKDOWN')
    print(dash)
    print('{:<10s}{:>14s}{:>16s}'.format('ASSET','VALUE','PERCENTAGE'))
    print(dash)
    
    for key,value in assets.items():
        print('{:<15s}$ {:>12.2f}{:>10.2%}'.format(key,value,value/networth))

    print(dash)
    print('{:<15s}${:>9.2f}\n'.format('NETWORTH',networth))
    return networth
    
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

    dash = '-' * 67 
    names = list(assets.keys())

    print("DETAILED FINANCIAL BREAKDOWN")
    # PRINT CASH ASSETS
    print(dash)
    print('{:<10s}{:>18s}{:>15s}{:>10s}'.format('ASSET','VALUE','% CLASS','% TOTAL'))
    print(dash)
    if total_cash != 0:
        print_asset(names[0],total_cash,total_cash/total_cash,total_cash/total_financial)
        print(dash)
        print_asset('TOTAL CASH',total_cash,total_cash/total_cash,total_cash/total_financial)
        print(dash + '\n')

    # PRINT BOND ASSETS
    if total_bonds != 0:
        print_asset(names[1],assets['Short Bonds'],assets['Short Bonds']/total_bonds,assets['Short Bonds']/total_financial)
        print_asset(names[2],assets['Medium Bonds'],assets['Medium Bonds']/total_bonds,assets['Medium Bonds']/total_financial)
        print_asset(names[3],assets['Long Bonds'],assets['Long Bonds']/total_bonds,assets['Long Bonds']/total_financial)
        print(dash)
        print_asset('TOTAL BONDS',total_bonds,total_bonds/total_bonds,total_bonds/total_financial)
        print(dash + '\n')

    # PRINT STOCK DETAILS
    if total_stocks != 0:
        print_asset(names[4],assets['Large Value'],assets['Large Value']/total_stocks,assets['Large Value']/total_financial)
        print_asset(names[5],assets['Large Blend'],assets['Large Blend']/total_stocks,assets['Large Blend']/total_financial)
        print_asset(names[6],assets['Large Growth'],assets['Large Growth']/total_stocks,assets['Large Growth']/total_financial)
        print_asset(names[7],assets['Mid Cap'],assets['Mid Cap']/total_stocks,assets['Mid Cap']/total_financial)
        print_asset(names[8],assets['Small Cap'],assets['Small Cap']/total_stocks,assets['Small Cap']/total_financial)
        print_asset(names[9],assets['Stocks'],assets['Stocks']/total_stocks,assets['Stocks']/total_financial)
        print(dash)
        print_asset('TOTAL STOCKS',total_stocks,total_stocks/total_stocks,total_stocks/total_financial)
        print(dash+'\n')

    # TOTAL FINANCIAL ASSETS
    print('{:<16s}{:>10s}{:>10.2f}'.format('TOTAL FINANCIAL ASSETS','$',total_financial))

    return total_financial

def print_asset(name,value,class_percent,total_percent):
    print('{:<16s}${:>12.2f}{:>14.2%}{:>10.2%}'.format(name,value,class_percent,total_percent))

def append_history(networth,financial_worth,fname='history.yaml'):

    today = date.today()
    today = today.strftime("%m/%d/%Y")

    if path.exists(fname):

        with open(fname) as f:
            load_history = yaml.safe_load(f)

        load_history[today] = [networth,financial_worth]

    else:
        load_history = {}
        load_history[today] = [networth,financial_worth]

    with open(fname,'w') as f:
        data = yaml.dump(load_history,f)


def pie_chart(asset_1,asset_2):
    total_asset_1 = sum(asset_1.values())
    total_asset_2 = sum(asset_2.values())

    data_1 = []
    data_2 = []

    account_1 = [] 
    account_2 = []

    for key,value in asset_1.items():
        if value==0:
            next 
        else:
            account_1.append(key)
            data_1.append(value)

    for key,value in asset_2.items():
        if value==0:
            next
        else:
            account_2.append(key)
            data_2.append(value)

    fig,(ax1,ax2) = plt.subplots(1,2,figsize=(11,8.5),subplot_kw=dict(aspect="equal"))

    def func(pct, sums):
        absolute = int(pct/100.*sums)
        return "{:.1f}%\n(${:d})".format(pct, absolute)

    wedges1, texts1, autotexts1 = ax1.pie(data_1,labels=account_1,autopct=lambda pct:func(pct,total_asset_1))
    wedges2, texts2, autotexts2 = ax2.pie(data_2,labels=account_2, autopct=lambda pct:func(pct,total_asset_2))

    ax1.legend(wedges1, account_1,title="Networth",
            loc="lower center",
            bbox_to_anchor=(0,0,0.5,1))

    ax2.legend(wedges2, account_2,title="Detailed Financials",
            loc="lower center",
            bbox_to_anchor=(1,0,0.5,1))


#    plt.setp(autotexts1,size=8,weight="bold")
#    plt.setp(autotexts2,size=8,weight="bold")

    ax1.set_title("Networth Breakdown")
    ax2.set_title("Detailed Financial")

    #plt.savefig('mygraph.pdf')
