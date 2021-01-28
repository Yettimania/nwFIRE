from os import listdir
from os.path import splitext

def print_create_menu():
    print(27*'-', 'CREATE MENU', 27*'-')
    print('1. Add Asset')
    print('2. Show portfolio summary')
    print('3. Save and Exit')
    print('4. Exit without Save')
    print(67*'-')

def print_edit_menu():
    print(27*'-', 'EDIT MENU', 27*'-')
    print('1. Add Asset')
    print('2. Drop Asset')
    print('3. Edit Asset')
    print('4. Summarize Portfolio')
    print('5. Exit & Save')
    print(67*'-')

def create_menu(portfolio):
    while True:
        print_create_menu()
        choice = input("Enter your choice [1-2]: ")
        if choice=='1':
            name = input("What is name of asset?: ").upper()
            portfolio.add(name)
        elif choice=='2':
            portfolio.summary()
        elif choice=='3':
            name = input("Enter portfolio name: ")
            name = str('./portfolios/' + name + '.yaml')
            print(name)
            portfolio.save(fname=name)
            print("Return to main menu")
            break
        elif choice=='4':
            break
        else:
            input("wrong Option selection. Enter any key to try again..")


def load_menu(portfolio):
    profiles = listdir('./portfolios/')
    fnames = [ x.split('.')[0] for x in profiles ] 
    print(67*'-')
    print("PROFILE LIST")
    print(67*'-')
    for idx,profile in enumerate(fnames):
        print('{}. {}'.format(idx+1,profile))
    selection = int(input("Select profile to load: "))
    profile = fnames[selection-1]
    path = str('./portfolios/' + profile + '.yaml')

    portfolio.load(fname=path)
    portfolio.summary()
    print("Portfolio loaded!")

def edit_menu(portfolio):
    while True:
        print_edit_menu()
        choice = input("Enter your choice [1-4]: ")
        if choice=='1':
            name = input("What is name of asset?: ").upper()
            portfolio.add(name)
        elif choice=='2':
            asset_list = portfolio.asset_list
            print("ASSET LIST")
            for asset in asset_list:
                print("- {}".format(asset))
            name = input("What is name of asset to drop?: ").upper()
            portfolio.drop(name)
        elif choice=='3':
            asset_list = portfolio.asset_list
            print("ASSET LIST")
            for asset in asset_list:
                print("- {}".format(asset))
            name = input("What is name of asset to edit?: ").upper()
            portfolio.edit(name)
        elif choice=='4':
            portfolio.summary()
        elif choice=='5':
            portfolio.save(portfolio.path)
            break
        else:
            input("Wrong Option selection. Enter any key to try again..")


def report_menu(portfolio):
    portfolio.report()
