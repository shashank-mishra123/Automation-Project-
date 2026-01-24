#create a base class vehicle and child class electricvehicle
class vehicle:
    def __init__(self):
        pass
    def wheels(self):
        print("four wheel")
    def bodyparts(self):
        print(" boby parts is same it")

class electricvehicle(vehicle):
    pass

electric = electricvehicle()
electric.wheels()
electric.bodyparts()
