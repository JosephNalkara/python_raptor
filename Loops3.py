binary = input("Enter a binary number : ")

if set(binary).issubset({'0','1'}):
    decimal = 0
    for digit in binary:
        decimal = decimal*2+int(digit)
    print("The decimal equivalent is : ",decimal)    

else:
    print("The binary you entered is invalid")    