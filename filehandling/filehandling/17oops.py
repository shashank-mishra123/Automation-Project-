#resolve method  conflicts using MRO()
class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):
        print("in B show")
class C(A):
    def show(self):
        print("in C show")
class D(B,C):
    pass
d=D()
d.show()
print(D.mro())
