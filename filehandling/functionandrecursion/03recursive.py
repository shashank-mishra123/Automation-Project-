# write a recursive function to print  number from 1 to  N
number = int(input("enter the number "))
def naturalnumber(number):
    if number>0:
        print(number)
        naturalnumber(number-1)
        

take = naturalnumber(number)
print(take)