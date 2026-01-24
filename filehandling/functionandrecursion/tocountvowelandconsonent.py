# a function to count vowel and consonent 
word ="shashank"
def check(word):
    count=0
    for indx in range(len(word)):
     if word[indx] =='a' or  word[indx]  =='e' or word[indx] =='i' or word[indx]  =='o' or word[indx]  =='u' :
        count +=1
    return count

num1=check(word)
print("vowel",num1)
print("consonent",len(word)-num1)
    
    
