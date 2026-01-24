# write afunction to check whether string is palindrome or not 
def check(strs):
    if strs==strs[::-1]:
        return"is palindrome"
    else:
        return"not"

strs = "naman"

s =check(strs)
print(s)