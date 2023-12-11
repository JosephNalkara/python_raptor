n = int(input("Enter how many natural numbers should be added: "))

i = 1  
sum = 0 

while i <= n:
    sum = sum+i
    i = i+1

print(f"The sum of the first {n} natural numbers is: {sum}")
