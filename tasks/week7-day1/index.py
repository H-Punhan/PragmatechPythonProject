#1 ------------------------------------------------------------------------------------------------------------
class User:
    def __init__(self,name) :
        self.name=name
    
    
    def Sayhello(self):
        print('helloo') # static method

    def __str__(self): #dunder method (special method )
        return self.name
    
u=User('Punhan')
print(u)
u.Sayhello()

#2 -------------------------------------------------------------------------------------------------------------
# inheritence
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


#3---------------------------------------------------------------------------------------------------------------------

# Başqa bir classdan miras alarkən miras aldığımız classın konsturktorunu yeniləmiş oluruq və buda
# həmin classın datalarının silinməsinə gətirib çixardır.Bu halın yaşanmaması üçün super() bizim köməyimizə çatır.
# Miras alınan classın init-ilə bizim init-metodumuz birləşir