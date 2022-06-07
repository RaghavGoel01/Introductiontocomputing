#Question 1
#To tell the grade of the user

#First we take marks of the user as input
marks=int(input("Enter your marks: "))

if marks>80:
    print(f"Your marks are {marks} and corresponding grade is A")
elif marks>60 and marks<=80:
    print(f"Your marks are {marks} and corresponding grade is B")
elif marks>50 and marks<=60:
    print(f"Your marks are {marks} and corresponding grade is C")
elif marks>45 and marks<=50:
    print(f"Your marks are {marks} and corresponding grade is D")
elif marks>25 and marks<=45:
    print(f"Your marks are {marks} and corresponding grade is E")
elif marks<=25:
    print(f"Your marks are {marks} and corresponding grade is F")

#Question 2
#Leap Year

#We take the year as input from the user
year=int(input("Enter the year: "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#Question 3
#Multiplication game

import random
for i in range(1,11,1):
    m=random.randrange(1,10,1) #Generates a random value from 1 to 10
    n=random.randrange(1,10,1) #Generates a random value from 1 to 10
    ans=int(input((f"Question {i}: {m}*{n} = ")))
    if m*n==ans:
    # if the answer is correct print right and start the next iteration
        print("Right!")
        continue
    else:
    # if the answer is incorrect print wrong and start the next iteration
        print("Wrong. The answer is ",m*n)
        continue

#Question 4
#Halloween Candy
n=1
while n<200:
    if n%5==2 and n%6==3 and n%7==2:
        print("Number of candies in the box are",n)
        break
    else:
        n+=1




