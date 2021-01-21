from asset import Asset

class Portfolio:
   
    def __init__(self):
        self.assets = [] 

    def add(self,name):
        self.assets.append(Asset(name))

    def drop(self,name):
        return None

    def edit(self,name):
        return None

    def save(self):
        return None 

    def read(self):
        return None

kyle = Portfolio()

kyle.add('FLS')
kyle.add('WFCHK')

for obj in kyle.assets:
    print(obj.name)
