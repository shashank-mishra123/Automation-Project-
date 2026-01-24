# create an abstract class bank with abstract method get_intrest_rate()
from abc import ABC , abstractmethod
class bank(ABC):
    @abstractmethod
    def get_intrest_rate(self):
        pass

class bob(bank):
    def get_intrest_rate(self):
        print("5% p to 10000")
b = bob()
b.get_intrest_rate()
