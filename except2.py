try:
    x,y = map(int,input("Enter the numerator and denominator").split())
    q = x//y
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print('You must enter two integers')
else:
    print('The quotient is ',q)
finally:
    print("Have a nice day")
