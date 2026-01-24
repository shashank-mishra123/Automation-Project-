#implementation sbi and hdfc classes using the abstract call bank
from abc import ABC , abstractmethod
class bank(ABC):
    @abstractmethod
    def banking(self):
        pass
class sbi(bank):
    def banking(self):
        print("welcome to sbi")
class hdfc(bank):
    def banking(self):
        print("welcome to hdfc ")

sb = sbi()
sb.banking()
hd = hdfc()
hd.banking()
