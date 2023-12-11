import math

a = int(input("Enter the first side length: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

peri = a + b + c
s = peri / 2
Area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("The perimeter is: ", peri)
print("And the area is: ", Area)
