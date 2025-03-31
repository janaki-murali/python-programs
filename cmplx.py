'''  Write Python program to create a class called as Complex to model complex numbers 
and implement _add_() and _mul_() methods to add and multiply two complex numbers. 
Display the result by overloading the + and * operators. (University Question June 2023)
'''

class Complex(object):
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def __add__(self,other):
        return Complex(self.real+other.real,self.imag+other.imag)
    def __mul__(self,other):
        return Complex(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
    def __str__(self):
        return str(self.real) + "{:+}".format(self.imag) + 'i'


a = Complex(10,-5)
b = Complex(-5,10)
print(a+b)
print(a*b)