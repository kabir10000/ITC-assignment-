'''
#Q1
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
print('Average: ',(a+b+c)/3)

# Q2
a = float(input("Gross Income: "))
b = float(input("No of Dependents: "))

taxable_income = a - 10000 - 3000*b
tax = taxable_income*0.2

if(taxable_income < 0):
    print("Tax: 0")
else:
    print("Tax: ", tax)


# Q3
a = int(input("number of seconds: "))
minutes = a//60
seconds = a % 60
print("Number of minutes:", minutes,
      "Number of seconds:", seconds)

# Q4
a = 25
b = "25"
c = 25.0

b = int(b)
c = int(c)
add = a+b+c
add = str(add)
print(add)


# Q5
import math


 
for i in range(0, 360, 15):
    j=math.radians(i)
    a=math.cos(j)
    b=math.sin(j)

    print(i,"---",round(b,4),round(a,4))

'''
