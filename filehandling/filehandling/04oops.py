#create the abstract class with both abstract and non abstract methods
from abc import ABC, abstractmethod
class simple(ABC):
    def __init__(self,name):
        self.name=name
    def call(self):
        print(self.name)
    @abstractmethod
    def abstr(self):
        pass

class medium(simple):
    def abstr(self):
       print("hi this is implementation")

medi = medium("ram")
medi.call()
medi.abstr()