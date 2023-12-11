import math

a=int(input("Enter the coefficient of x^2 : "))

b=int(input('Enter coefficient of x : '))

c=int(input('Enter the constent term : '))

d=(-b + math.sqrt(b**2 - (4*a*c))) / (2*a)

e=(-b - math.sqrt(b**2 - (4*a*c))) / (2*a)

print('The roots of the quadratic equation is : ',d, ' and ',e)