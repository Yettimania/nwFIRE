from portfolio import Portfolio
import submenu

portfolio = Portfolio()


print("nwFIRE v0.1 - Tracking Your Independence")

submenu.startup(portfolio)

def print_menu():
    print(30 * "-" , "MENU" , 31 * "-")
    print("1. Create Portfolio")
    print("2. Load Portfolio")
    print("3. Edit Portfolio")
    print("4. Report Portfolio")
    print("5. Plot networth history")
    print("6. Forecast Portfolio")
    print("7. Exit")
    print(67 * '-')

loop = True

while loop:
    print_menu()
    choice = input("Enter your choice [1-6]: ")

    if choice=='1':
        submenu.create_menu(portfolio)
    elif choice=='2':
        submenu.load_menu(portfolio)
    elif choice=='3':
        submenu.edit_menu(portfolio)
    elif choice=='4':
        submenu.report_menu(portfolio)
    elif choice=='5':
        submenu.history_menu(portfolio)
    elif choice=='6':
        submenu.forecast_menu(portfolio)
    elif choice=='7':
        loop=False
    else:
        input("Wrong option selection. Enter any key to try again..")

