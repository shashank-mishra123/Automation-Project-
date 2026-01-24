#create a class with protected  variable _discount
class Class():
    def __init__(self):
        self._discount=500

class c1(Class):
    def acess(self):
        self._discount=400
    def acess2(self):
        print(self._discount)
c = c1()
c.acess2()