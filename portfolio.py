class Portfolio:
   
    def __init__(self,fname=None):
        self.__assets = {}
        if fname is not None:
            return 0

    def list_assets(self):
        print("Assets within portfolio:")
        print(list(self.__assets.keys()))
        return list(self.__assets.keys())

    def add(self,name):
        print("Selection of asset types:")
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
        self.__assets.pop(name,None)
        print(self.__assets)

    def edit(self,name):
        if self.__assets.get(name) is not None:
            attributes  = self.__assets.get(name)
        print(f'Attributes of {name}:')
        for index,item in enumerate(list(attributes.keys())):
            print(index,item)
        index = int(input(f'Select attribute to edit: '))
        selection = list(attributes.keys())[index]
        value_type = type(self.__assets[name][selection])
        print(value_type)
        if value_type is str:
            value = input(f'Enter value for attribute: ')
            self.__assets[name][selection] = str(value)
        if value_type is float:
            value = input(f'Enter value for attribute: ')
            self.__assets[name][selection] = float(value)
        if value_type is list:
            cash,bonds,stocks = [float(x) for x in input("Enter composition of cash,bonds,stocks: ").split(',')]
            composition = [cash,bonds,stocks]
            self.__assets[name][selection] = composition 
        
        print(self.__assets[name])                      
                                                        
    def write(self):
        return None 

    def read(self):
        return None

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
        self.__assets[name] = {'value':amount,'type':'cash'}

    def _add_investment(self,name):
        shares = input(f'Number of owned shares for {name}: ')
        category = self._morningstar_grid()
        cash,bonds,stocks = [float(x) for x in input("Enter composition of cash,bonds,stocks: ").split(',')]
        composition = [cash,bonds,stocks]
        self.__assets[name] = {'shares':float(shares),'type':'investment','category':category, 'composition':composition} 
    
    def _add_realestate(self,name):
        amount = input(f'Amount of equity for {name} property: ')
        self.__assets[name] = {'value':int(amount),'type':'realestate'}

    def _add_equity(self,name):
        amount = input(f'Amount of equity for {name} business: ')
        self.__assets[name] = {'value':int(amount),'type':'equity'}

kyle = Portfolio()

kyle.add('LLL')
kyle.add('WFCHK')
kyle.list_assets()
kyle.edit('LLL')

