# write a function check number is prime or not 
number =7

def isprime(number):
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count+=1
    return count

ret = isprime(number)
#print(ret)
if(ret==2):
    print(" number is prime ")
else:
    print("number is not prime")
