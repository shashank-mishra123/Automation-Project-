# write a program to check whether number is even or odd using function
def check(num):
    if num%2==0:
        return"even"
    else:
        return"odd"

s = check(89)
print(s)