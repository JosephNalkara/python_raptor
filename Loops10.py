num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)
sum_of_digits = 0

for digit in num_str:
    sum_of_digits += int(digit) ** num_digits

if num == sum_of_digits:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
