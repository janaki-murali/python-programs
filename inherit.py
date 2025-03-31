class A(object):
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        A.__init__(self)
        super().__init__()

class C(B,A):
    def __init__(self):
        print("C")
        super().__init__()

print("An object of B next")       
b = B()
print("An object of C next")
c = C()
