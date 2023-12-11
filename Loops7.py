n = int(input("Enter a number: "))

n1 = n*n

a = n1%10

if n==a:
    print("The number ", n , " is automorphic")

else:
    print("The number is not automorphic.")    