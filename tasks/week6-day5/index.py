class Restoran:
    def __init__(self,ad,metbex_novu) -> None:
        self.ad=ad
        self.metbexnovu=metbex_novu
        self.isOpen=True
    
    def describe(self):
        print(f'{self.ad}-{self.metbexnovu}')

    def openrestoran(self):
        if self.isOpen==True:
            print('acigdir')
        else:
            print('aciqdeyil')

r=Restoran('Lorem','ipsum')
r.newword='a'
print(r.newword)
r.describe()
r.openrestoran()
r=Restoran('Lore','ipsu')
r.isOpen=False
r.describe()
r.openrestoran()