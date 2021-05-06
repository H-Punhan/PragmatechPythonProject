# Inheritance

class Car:
  
    
   

    def __init__(self,enginevalue,color):
        self.engine='off'
        self.enginevalue=enginevalue
        self.color=color

    def enginepower(self):
       
        if self.engine=='off':
            self.engine='on'
            print(f'engine is {self.engine}')
        else:
            self.engine='off'
            print(f'engine is {self.engine}')

    
    

class Car2(Car):
    def __init__(self,enginevalue,color,brand='bmw'):
        super().__init__(enginevalue,color)
        self.brand=brand

    

c=Car2('2','Black','Bmw')
c.enginepower()
