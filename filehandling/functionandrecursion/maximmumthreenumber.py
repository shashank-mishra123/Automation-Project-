# write a function that return the maximum of three number
def maxthree(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

maximum = maxthree(0,89,9)
print(maximum)