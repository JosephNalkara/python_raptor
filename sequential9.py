t=int(input('Enter the total mark for a subject : '))

a=int(input('Enter the mark you got for first subject : '))
b=int(input('Enter the mark you got for second subject : '))
c=int(input('Enter the mark you got for third subject : '))
d=int(input('Enter the mark you got for fourth subject : '))
e=int(input('Enter the mark you got for fifth subject : '))

tm=a+b+c+d+e
mt=t*5

per=(tm/mt)*100

print('The percentage is : ',per)