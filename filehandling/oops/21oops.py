# demonstrate the runtime polymorphism using inhertitance
class Animal:
    def sound(self):
        print(" is animal")
class dog(Animal):
    def sound(self):
        print(" in  dog")


def make_sound(animal):
    animal.sound()

animals = Animal()
make_sound(animals)

dogs = dog()
make_sound(dogs)