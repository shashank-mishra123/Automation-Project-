# demonstrate the method overriding in real world example 
class bank:
    def rate_of_interest(self):
        return 0
class sbi(bank):
    def rate_of_interest(self):
        return 7.5
class icici(bank):
    def rate_of_interest(self):
        return 8.5
class axis(bank):
    def rate_of_interest(self):
        return 9.5
sbi_bank = sbi()
icici_bank = icici()
axis_bank = axis()
print("SBI Rate of Interest:", sbi_bank.rate_of_interest())
print("ICICI Rate of Interest:", icici_bank.rate_of_interest())
print("AXIS Rate of Interest:", axis_bank.rate_of_interest())
