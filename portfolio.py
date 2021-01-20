class Portfolio:
   
    def __init__(self):
        self.__cash = {}
        self.__investment = {} 
        self.__realestate = {}
        self.__equity = {}

    def add(self,name):

        selection = self._asset_prompt(name)

        if selection == '1':
            self._add_cash(name)
        elif selection == '2':
            self._add_investment(name)
        elif selection == '3':
            self._add_realestate(name)
        elif selection == '4':
            self._add_equity(name)
        else:
            print("Unknown selection.") 

    def delete(self,name):
        self.__cash.pop(name,None)
        self.__investment.pop(name,None)
        self.__realestate.pop(name,None)
        self.__equity.pop(name,None)
        print(self.__investment)

    def edit(self,name):
        if self.__cash.get(name) is not None:
            x = self.__cash.get(name)
            print(f'Values to change for {name} asset: {x.keys()}')
            key = input('Enter key to change: ')
            value = input('Enter value to change to: ')
            self.__cash[name].update(key = value)
            print(self.__cash[name])
        if self.__investment.get(name) is not None:
            x = self.__investment.get(name,None)
            print(f'Values to change for {name} asset: {x.keys()}')
            key = input('Enter key to change: ')
            value = input('Enter value to change to: ')
            self.__investment[name].update(key = value)
            print(self.__investment[name])
        if self.__realestate.get(name) is not None:
            x = self.__realestate.get(name,None)
            print(f'Values to change for {name} asset: {x.keys()}')
            key = input('Enter key to change: ')
            value = input('Enter value to change to: ')
            self.__realestate[name].update(key = value)
            print(self.__realestate[name])
        if self.__equity.get(name) is not None:
            x = self.__equity.get(name,None)
            print(f'Values to change for {name} asset: {x.keys()}')
            key = input('Enter key to change: ')
            value = input('Enter value to change to: ')
            self.__equity[name].update(key = value)
            print(self.__equity[name])

    def _asset_prompt(self,name):
        menu = {}
        menu['1'] = "Cash"
        menu['2'] = "Investment"
        menu['3'] = "Real Estate"
        menu['4'] = "Owner Equity"

        options = menu.keys()
        for entry in options:
            print(entry,menu[entry])
        
        selection = input(f'Select asset type to {name}: ')

        return selection

    def _morningstar_grid(self):
        menu = {}
        menu['1'] = 'Large Value'
        menu['2'] = 'Large Blend'
        menu['3'] = 'Large Growth'
        menu['4'] = 'Medium Value'
        menu['5'] = 'Medium Blend'
        menu['6'] = 'Medium Growth'
        menu['7'] = 'Small Value'
        menu['8'] = 'Small Blend'
        menu['9'] = 'Small Growth'
        
        options = menu.keys()
        for entry in options:
            print(entry,menu[entry])
        
        selection = input("Select Morningstar Category: ")

        category = menu[selection]

        return category 

    def _add_cash(self,name):
        amount = input(f'Amount $ in {name} account: ')
        self.__cash[name] = amount

    def _add_investment(self,name):
        shares = input(f'Number of owned shares for {name}: ')
        category = self._morningstar_grid()
        cash,bonds,stocks = [float(x) for x in input("Enter composition of cash,bonds,stocks: ").split(',')]
        composition = [cash,bonds,stocks]
        self.__investment[name] = {'shares':float(shares),'category':category, 'composition':composition} 
    
    def _add_realestate(self,name):
        amount = input(f'Amount of equity for {name} property: ')
        self.__realestate[name] = int(amount)

    def _add_equity(self,name):
        amount = input(f'Amount of equity for {name} business: ')
        self.__realestate[name] = int(amount)
        
kyle = Portfolio()

kyle.add('LLL')
kyle.edit('LLL')

