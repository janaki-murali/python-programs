x,y = map(int,input("Enter the numerator and denominator").split())
try:
    q = x//y
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print('The quotient is ',q)