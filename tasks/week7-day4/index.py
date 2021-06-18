#1 ----------------------------------------------------------------------------------------------------------

class Blog:
    def __init__(self,title,content):
        self.title=title
        self.content=content
    
    def __str__(self):
        return self.title

# b=Blog('Python tips','text')
# print(b)
# b=Blog('Frameworks for python','text')
# print(b)
# b=Blog('OOP starting','text')
# print(b)

#2 ---------------------------------------------------------------------------------------------------------------

class Userlogin:
    def __init__(self,username,password):
        self.__username=username
        self.__password=password
    
    def login(self):
        print('signed')

u=Userlogin('punhan',12345)
# u.login()

#3 ------------------------------------------------------------------------------------------------------------

from abc import ABC,abstractclassmethod

class Tech(ABC):

    @abstractclassmethod
    def on(self):
        pass

class Phone(Tech):
    
    def on(self):
        print('Phone is on')

class Pc(Tech):
    
    def on(self):
        print('Pc is on')

# p=Phone()
# p.on()

# pc=Pc()
# pc.on()

