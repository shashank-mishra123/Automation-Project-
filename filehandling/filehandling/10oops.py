#prevent the direct modification of the account balance
class User_Account():
    def __init__(self):
        self.__account_balance=10000

    @property
    def get_balance(self):
        return self.__account_balance
    
    @property
    def set_balance(self):
        if (self.isAdmin()=="yes"):
            return self.__account_balance+1000
        else:
            return "sorry to changes not allows here"
    
    def isAdmin(self):
        if(self.__account_balance<1000):
            return "yes"
        else:
            return "no"
user = User_Account()
print(user.get_balance)
print(user.set_balance)