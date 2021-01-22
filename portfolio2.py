from asset import Asset
import yaml

class Portfolio:
   
    def __init__(self):
        self.assets = [] 

    def add(self,name):
        self.assets.append(Asset(name))

    def drop(self,name):
        for i,obj in enumerate(kyle.assets):
            if obj.name == name:
                kyle.assets.pop(i)
                exit 

    def edit(self,name):
        for obj in self.assets:
            if obj.name == name:
                obj.edit()
                exit 

    def save(self,fname='portfolio.yaml'):
        dict_list = []
        for obj in kyle.assets:
            obj_dict = obj.__dict__
            dict_list.append(obj_dict)
        with open(fname,'w') as f:
            data = yaml.dump(dict_list,f)

    def load(self,fname='portfolio.yaml'):
        with open(fname) as f:
            assets = yaml.full_load(f)

        self.assets = [] 
        for asset in assets:
            x = Asset(...,load=True)
            x.name = asset['name'] 
            x.category = asset['category'] 
            x.amount = asset['amount'] 
            x.mstar = asset['mstar'] 
            x.composition = asset['composition'] 
            x.ticker = asset['ticker'] 
            self.assets.append(x)

    def summary(self):
        dash = '-' * 30
        print(dash)
        print('{:<10s}{:>4s}{:>12s}'.format('ASSET','CATEGORY','AMOUNT'))
        print(dash)
        for obj in self.assets:
            asset = obj.name
            category = obj.category
            amount = obj.amount
            print('{:<10s}{:<15s}{:>1f}'.format(asset,category,amount))
    
    def detail(self,name):
        for obj in self.assets:
            if obj.name == name:
                print("SUMMARY OF ASSET:")
                print(f'Name: {obj.name}\nCategory: {obj.category}\nAmount: {obj.amount}\n\
MStar: {obj.mstar}\nComposition: (c/b/s): {obj.composition}\nTicker: {obj.ticker}')


    @property
    def asset_list(self):
        asset_list = []
        for obj in self.assets:
            asset_list.append(obj.name)
        return asset_list

kyle = Portfolio()
#kyle.add('LLL')
#kyle.add('FLS')
#
#kyle.save()
kyle.load()
kyle.summary()
kyle.detail('FLS')
print(kyle.asset_list)
#for obj in kyle.assets:
#    print(obj.__dict__)
