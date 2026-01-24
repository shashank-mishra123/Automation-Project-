# write a function to print number N to 1 .
number = int(input("enter the number "))
def printnumber(number):
    if number < 0:
        print(number)
        printnumber(number-1)
take = printnumber(number)
print(take)