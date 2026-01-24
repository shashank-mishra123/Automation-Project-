# write a function that accepts a list of number and return a new list of only even number
l = [1,2,3,4,5,6,7,8,9,10]
def retuneven(l):
    num = []
    for indx in l:
        if indx%2==0:
         num= num.insert(indx)
    return num

take = retuneven(l)
print(take)