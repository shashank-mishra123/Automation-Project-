# print the recursive function to find the factorial of a number.
number = 5
def factorial(number):
    if  number ==0 :
        return 1
    else :
        return number*factorial(number-1)


take = factorial(number)
print(take)