n = int(input("Enter a number : "))
temp = n 
rev = 0

while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

if temp == rev:
    print("The number", temp, "is a palindrome number")
else:
    print("The number is not a palindrome.")
