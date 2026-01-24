# write a function that word with multiple object type 

class college:
    def __init__(self,fess,name):
        self.fess=fess
        self.name=name
    def show(self):
        print("fess =",self.fess," name=",self.name)

class Bca:
    def __init__(self,fess,name):
        self.fess = fess
        self.name = name
    def show(self):
        print(" fess =",self.fess," name =",self.name)


def detield(give):
    give.show()

colege = college(5000000,"united")
bca = Bca(74800,"computer science")

detield(colege)
detield(bca)

