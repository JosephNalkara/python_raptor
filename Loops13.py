x = int(input("Enter the base: "))
n = int(input("Enter the power: "))

result = 1
i = 0

while i < n:
    result *= x
    i += 1

print("Result:", result)
