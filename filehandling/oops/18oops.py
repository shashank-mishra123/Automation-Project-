# Decoretors
def deco(hello):
    def wrapper():
        print(" transaction start .....")
        hello()
        print(" transaction is ending .....")
    return wrapper

def hello():
    print(" excution all the step ....")

hello = deco(hello)
hello()