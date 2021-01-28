from portfolio import Portfolio
import submenu

portfolio = Portfolio()

def print_menu():
    print(30 * "-" , "MENU" , 31 * "-")
    print("1. Create Portfolio")
    print("2. Load Portfolio")
    print("3. Edit Portfolio")
    print("4. Report Portfolio")
    print("5. Forecast Portfolio")
    print("6. Exit")
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
        print("Menu 5 has been selected")
    elif choice=='6':
        print("Menu 6 has been selected")
        loop=False
    else:
        input("Wrong option selection. Enter any key to try again..")

