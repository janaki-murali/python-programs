'''Question no. 18a from 2022 university question paper'''
''' Create an Abstract Base Class called Shape that include abstract methods area() and circumference().
Then derive two classes Circle and Rectangle from the Shape class and implement the area() and 
circumference() methods . Write a Python program to implement above concept.
'''
'''
***Abstract Methods***
Abstract methods are methods that are defined in an abstract class but do not have an implementation.
They serve as a blueprint for the subclasses, ensuring that they provide their own implementation.
'''

from abc import ABC,abstractmethod 
''' ABCs allow you to define common interfaces that various subclasses can implement while 
enforcing a level of abstraction. Python provides the abc module to define ABCs and enforce 
the implementation of abstract methods in subclasses.

'''
from math import pi
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth  
    def perimeter(self):
        return 2 * (self.length+self.breadth)
    def __str__(self):
        return "Rectangle: Length = "+ str(self.length)+" Breadth = "+str(self.breadth)

class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = 0.5 * (self.a+self.b+self.c)
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
    def perimeter(self):
        return self.a+self.b+self.c
    def __str__(self):
        return "Triangle with sides: a = " + str(self.a) + \
              " b = " + str(self.b) + " c = " + str(self.c)

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2
    def perimeter(self):
        '''Perimeter is circumference'''
        return 2 * pi * self.radius
    def __str__(self):
        return "Circle: Radius = "+ str(self.radius)

r1 = Rectangle(10,8)   
print(r1) 
print(r1.area(),r1.perimeter())
c1 = Circle(10)
print(c1)
print(c1.area(),c1.perimeter())
t1 = Triangle(3,6,7)
print(t1)
print(t1.area(),t1.perimeter())
