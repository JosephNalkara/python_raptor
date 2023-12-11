a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(a+1, b):
    square = i ** 2
    print("Square of", i, "is", square)
