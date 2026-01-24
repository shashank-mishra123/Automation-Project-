# write a function that return the second largest number from alist (handle duplicat)
l1 =[1,2,3,4,5,3,4,6]

def secondlargest(l1):
    set1 =list(set(l1))
    list.sort(set1)
    return (set1[-2])
take = secondlargest(l1)
print(take)