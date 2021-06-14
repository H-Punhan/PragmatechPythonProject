#2 inheritence
class Tempcar:
    def __init__(self,motor,atgucu):
        self.motor=motor
        self.atgucu=atgucu

    def nitro(self):
        print('nitro verildi')
    
class Car(Tempcar):
    
    def __init__(self, motor, atgucu,brand):
        self.brand=brand
        super().__init__(motor,atgucu)

c=Car(2.3,200,'bmw')
# c.nitro()

#-----------------------------------------------------
#polymorphism

class Otyeyenler:
    def __init__(self,name) :
        self.name=name
    def qidanlanma(self):
        print(f'{self.name} ot ile qidalanir ')

class Etyeyenler:
    def __init__(self,name) :
        self.name=name
    def qidanlanma(self):
        print(f'{self.name} et ile qidalanir')

o=Otyeyenler('Qoyun')
e=Etyeyenler('Peleng')
#o.qidanlanma()
#e.qidanlanma()