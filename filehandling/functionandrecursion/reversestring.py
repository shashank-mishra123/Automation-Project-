# write function to reverse a string without using a sclicing
name ="shashank"
print(len(name))
def reversestring(name):
    num= ''
    for char in name:
        num = char+num
    return num
Call = reversestring(name)
print("reverse strinf :", Call)
