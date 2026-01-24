# create an abstract class vehicele with an abstratct method  start(). implement 
#it car and bike classe
from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicle):
    def __init__(self,carname):
        self.carname=carname
    def start(self):
       print("car is ",self.carname)

class bike(vehicle):
    def __init__(self,bikename):
        self.bikename=bikename
    def start(self):
        print(f'bike is {self.bikename}')
bike1 = bike("honda")
bike1.start()
car1 = car("maruri")
car1.start()

       
        