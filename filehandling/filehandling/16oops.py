# create a hierachical inheritance with  proper uese of super() method
class Animal:
    def __init__(self):
        print("I am an animal")
    
    def eat(self):
        print("I can eat")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("I am a dog")

    def bark(self):
        print("I can bark")

class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("I am a cat")

    def meow(self):
        print("I can meow")
dog = Dog()
dog.eat()
dog.bark()
cat = Cat()
cat.eat()
cat.meow()
