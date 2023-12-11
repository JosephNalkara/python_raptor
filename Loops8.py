number = int(input("Enter the number: "))
total = 0

for i in range(1, number + 1):
    if number % i == 0:
        total += i

print("The sum of factors of", number, "is", total)
