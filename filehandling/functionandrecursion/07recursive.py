# to find power of a*b using recursive function
a = 2
b = 4
def power(a,b):
    if b >0:
        return a*power(a,b-1)
take = power(a,b)
print(take)
    
