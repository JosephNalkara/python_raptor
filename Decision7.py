num = int(input("Enter a two digit number : "))

if num<10 or num>99:
    print("Invalid number")

else:
    n1=num//10

    n2=num%10

    if n1>n2:
        print(n2," Is the smaller number")

    else:
        print(n1," Is the smallest number")    