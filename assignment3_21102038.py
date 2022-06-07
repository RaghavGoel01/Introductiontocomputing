#Question 1
#To find binary equivalent

a=int(input("Enter a number: "))
bin_a=bin(a)
print(bin_a)

#Question 2
#Calculator Program

# Function to add two numbers
def add(num1, num2):
	return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
	return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
	return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
	return num1 / num2

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 : "))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=",add(number_1, number_2))

elif select == 2:
	print(number_1,"-", number_2,"=",subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=",divide(number_1, number_2))
else:
	print("Invalid input")

#Question 3
#Python Expressions
import math

#a)
print((3+4)*5)

#b)
n=int(input("Enter the value of n: "))
print((n*(n-1))/2)

#c)
r=int(input("Enter the value of r: "))
print(4*r*r*math.pi)

#d)
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
print(math.sqrt(r*math.pow(math.cos(a),2)+r*math.pow(math.sin(b),2)))

#e)
x1=int(input("Enter value of x1: "))
x2=int(input("Enter value of x2: "))
y1=int(input("Enter value of y1: "))
y2=int(input("Enter value of y2: "))
print((y2-y1)/(x2-x1))


#Question 4
#Range Expressions

#a)
for i in range(5):
	print(i)
print()

#b)
for i in range(3,10):
	print(i)
print()

#c)
for i in range(4,13,3):
	print(i)
print()

#d)
for i in range(15,5,-2):
	print(i)
print()

#e)
for i in range(5,3):
	print(i)
print()

#Question 5
#To calculate molecular weight

h=int(input("Enter no of hydrogen atoms: "))
c=int(input("Enter no of carbon atoms: "))
o=int(input("Enter no of oxygen atoms: "))
#we take the no of individual atoms in carbohydrate as input fromt the user

weighth=1.00794
weightc=12.0107
weighto=15.9994
#atomic weight of hydrogen, carbon and oxygen  are stored as variables
weight=h*weighth+c*weightc+o*weighto
print("Molecular weight of the compound is ",weight)
