from asset import Asset
import report
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
            x.retirement = asset['retirement']
            x.amount = asset['amount'] 
            x.composition = asset['composition'] 
            x.comp_type = asset['comp_type']
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
            print('{:<10s}{:<15s}{:>1.3f}\n'.format(asset,category,amount))
    
    def detail(self,name):
        dash = '-' * 30
        for obj in self.assets:
            if obj.name == name:
                print(dash)
                print(f"SUMMARY OF {obj.name}")
                print(dash)
                print(f'Name: {obj.name}\nCategory: {obj.category}\nAmount: {obj.amount}\nComposition: (c/b/s): {obj.composition}\nComposition Type: {obj.comp_type}\nTicker: {obj.ticker}\nRetirement: {obj.retirement}\n')

    def report(self):
        asset_sum = report.asset_dict()
        detail_sum = report.detailed_dict()

        for obj in self.assets:
            if obj.category == 'Cash':
                asset_sum['Cash'] += obj.amount
                detail_sum['Cash'] += obj.amount
            elif obj.category == 'Real Estate':
                asset_sum['RealEstate'] += obj.amount
            elif obj.category == 'Owner Equity':
                asset_sum['Equity'] += obj.amount
            else:
                cash_value = 0.0
                bond_value = 0.0
                stock_value = 0.0

                total_value = obj.amount * obj.value
                cash_value = total_value * obj.composition[0]
                asset_sum['Cash'] += cash_value
                detail_sum[obj.comp_type[0]] += cash_value

                bond_value = total_value * obj.composition[1]
                asset_sum['Bonds'] += bond_value
                detail_sum[obj.comp_type[1]] += bond_value

                stock_value += total_value * obj.composition[2]
                asset_sum['Stocks'] += stock_value 
                detail_sum[obj.comp_type[2]] += stock_value

        report.networth(asset_sum)
        report.financial_breakdown(detail_sum)

    @property
    def asset_list(self):
        asset_list = []
        for obj in self.assets:
            asset_list.append(obj.name)
        return asset_list

kyle = Portfolio()
#kyle.add('LLL')
#kyle.add('FLS')
#kyle.add('XXX')
#kyle.save()
kyle.load()
kyle.report()
#kyle.detail('LLL')
#print(kyle.asset_list)
#for obj in kyle.assets:
#    print(obj.__dict__)
