# show how super() working internally
class parent:
    def __init__(self,address):
        self.address=address
        self._mobno="123456789"

class child(parent):
    def __init__(self, address):
        super().__init__(address)
    
    def name(self):
        print("sitaram")

parentes = parent("prayagraj")
childs = child()

print("addreass is", childs.address)
childs.name()