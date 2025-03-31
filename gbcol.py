from student import Student
'''Demonstrate unreferenced object for garbage collection'''
s = Student("Sam",5)
l = [s]
print(l)
l.pop()
print(s)
s=None
print(s)
print(l)
