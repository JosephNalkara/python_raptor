n = int(input("Enter the number : "))

rev = 0

while n>0:
    a = n % 10
    rev = rev * 10 + a
    n = n//10


print("The reverse of the number you entered is : ",rev)    