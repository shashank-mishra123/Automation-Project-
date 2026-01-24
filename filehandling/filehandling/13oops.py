# show how name magling working in pyhton
class employee():
    def __init__(self):
        self.__varible=500
    def get_varible(self):
        print(self.__varible)

emp = employee()

print(emp._employee__varible)