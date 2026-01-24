#create diffrent classes with same method name and signature
class parent:
    def same(self):
        print(" is in parent class with same function ")
    def signature(self):
        print(" is in parent class signature")
class child1():
    def same():
        print(" is in child1  with same function ")
    def signature():
        print(" is in parent childs1 signature")
    
class child2():
    def same():
        print(" is in childs2 same method ")
    def signature():
        print(" is in parent childs2 signature")

par = parent()
par.same()
par.signature()