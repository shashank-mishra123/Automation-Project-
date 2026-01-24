# create an abstract class shape with an abstract method arae () . impelement for rectangle and circlr.
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,lenght,breath):
        self.lenght=lenght
        self.breath = breath
    def area(self):
        print(self.lenght*self.breath)

class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print(3.14*self.radius*self.radius)
    

rec = rectangle(2,3)
rec.area()
cir = circle(4)
cir.area()



