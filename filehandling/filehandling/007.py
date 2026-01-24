# create a real world abstraction example of abstract class
from abc import ABC , abstractmethod
class college(ABC):
    @abstractmethod
    def faclluty_name(self):
        pass
class BCA(college):
    def faclluty_name(self):
       print("gaurav sirvastava,anjney awasthi")

class BBA(college):
    def faclluty_name(self):
        print("aman sirvastva,sudhanshu tiwari")

Bca = BCA()
Bca.faclluty_name()
bba = BBA()
bba.faclluty_name()
