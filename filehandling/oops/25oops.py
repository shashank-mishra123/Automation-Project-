# demonstrate the polymorphisms in loop
class circle:
    def __init__(self,radus):
        self.radus=radus
    def area(self):
        return 3.14*self.radus*self.radus
class rectangle:
    def __init__(self,lenght,breath):
        self.lenght=lenght
        self.breath=breath
    def area(self):
        return self.lenght*self.breath
shapes=[circle(4),rectangle(2,3)]
for shape in shapes:
    print("area is:",shape.area())  
        