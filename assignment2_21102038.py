# QUESTION-1

string='Python is a case sensitive language.'

# PART-(a)
# We use len() function to find string length
print(len(string))

# PART-(b)
# We reverse tthe order of the string
print(string[len(string)::-1])

# PART-(c)
# Slicing of string
print(string[10:26])

# PART-(d)
# String replacement
print(string.replace("a case sensitive", "object oriented"))

# PART-(e)
# String index
print(string.index("a"))

# PART-(f)
# String removal
print(string.replace(" ", ""))


# QUESTION-2
# STRING FORMATTING

# First we take input of data from user
name=input("Enter your name: ")
SID=input("Enter your SID: ")
dep_name=input("Enter your department name: ")
CGPA=input("Enter your CGPA: ")

# Then we print the output using string formatting
print(f'Hey, {name} Here!')
print(f'My SID is {SID}')
print(f'I am from {dep_name} department and my CGPA is {CGPA}')


# QUESTION-3

a=56
b=10

# PART-(a)
print(a&b)

# PART-(b)
print(a|b)

# PART-(c)
print(a^b)

# PART-(d)
print(a<<2)
print(b<<2)

# PART-(e)
print(a>>2)
print(b>>4)


# QUESTION-4
# CHECKING PRESENCE OF "NAME"

# First we take user input
string=input("Enter your string: ")

# Then we check if "name" is present in string or not
if "name" in string:
    print('Yes')
else:
    print('No')


#QUESTION 5
#CHECKING FOR TRIANGLE

#First we take user input
a1=input("Enter 1st side: ")
b1=input("Enter 2nd side: ")
c1=input("Enter 3rd side: ")

#Then we convert them into integers
a=(int)(a1)
b=(int)(b1)
c=(int)(c1)

# Then we check the condition for triangle
if((a+b)>c and (b+c)>a and (c+a)>b):
    print('Yes')
else:
    print('No')

# QUESTION 6
# NO OF BITS

a=10
b=99

# initially setbits is equal to 0
setbits = 0
     
    # & each bits of a && b with 1
    # and store them if t1 and t2 are not equal
    # if t1 != t2 then we will flip that bit
while(a > 0 or b > 0):
        t1 = (a & 1)
        t2 = (b & 1)
        if(t1 != t2):
            setbits += 1
             
        # right shifting a and b by 1 bit
        a>>=1
        b>>=1
print(setbits)