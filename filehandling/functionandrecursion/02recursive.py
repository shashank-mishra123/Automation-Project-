# write arecursive function to find the sum of N natural number .
number = int ( input("enter the number "))

def naturalnumber(number):
    if number ==0:
        return 1
    else :
        return number+naturalnumber(number-1)
take = naturalnumber(number)
print(take-1)