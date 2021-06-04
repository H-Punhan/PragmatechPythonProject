class Car:
    def __init__(self,reng,motor,ad):
        self.name=ad
        self.color=reng
        self.motor=motor
    
   
    def __str__(self) -> str:
        return self.name


bmw=Car('black','2','bmw')
mercedes=Car('black','2','mercedes')
mazda=Car('black','2','mazda')
print(bmw,mercedes,mazda)