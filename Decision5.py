a=int(input("Enter coefficient of x^2 : "))
b=int(input("Enter coefficient of x : "))
c=int(input("Enter the constant term : "))

d=(((b)^2)-(4*a*c))

if d>=0:
    if d==0:
        print("The quadratic equation with these coefficient has one real and repeated solution")

    else:
        print("This quadratic equation with these coefficient have two real and distinct solution")
else:
    print("This quadratic equation with these coefficient has no real solution, but two complex solution")

print(d)