num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
temp1 = num1
temp2 = num2

while num2:
    num1, num2 = num2, num1 % num2

gcd = num1

print("The GCD of", temp1, "and", temp2, "is", gcd)
