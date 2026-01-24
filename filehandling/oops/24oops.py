# implement operator overloading using _mul_().
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __mul__(self, other):
        if isinstance(other, int):
            return self.price * other
        return NotImplemented
product = Product("laptop", 50000)
total_cost = product * 3
print("Total cost for 3 laptops:", total_cost)
