class User:
    def __init__(self,name,surname,addres):
        self.name=name
        self.surname=surname
        self.__addres=addres
    
    def getAddres(self):
        return self.__addres
    
    def setAddres(self,a):
        self.__addres=a

    prop=property(getAddres,setAddres)

u=User('Punhan','Huseynov','Kenya')

print(u.prop)

u.prop='Cuba'

print(u.prop)
    
