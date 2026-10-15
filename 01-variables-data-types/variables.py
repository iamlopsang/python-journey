        ## Python Variables  ##

## Creating variables
name = "Alex"
age = 25

print(name)     #Alex
print(age)      #25

# Variable naming rules
# 1. Variable names must start with a letter or an underscore (_).
# 2. Variable names cannot contain spaces.
# 3. Variable names are case-sensitive.

## Valid naming examples of variables:

name = "John"
student_name = "Alice"
_age = 30
price1 = 9.99

# Invalid naming examples of variables:
# 1name = "Invalid"   # Starts with a number
# name 1 = "Invalid"  # Contains a space
# Name = "Invalid"   # Case-sensitive, different from 'name'

# Note: age, Age, and AGE are considered different variables in Python.
#   Python is case-sensitive, so variable names with different cases are treated as distinct variables.

## Multi words variable names:

student_name = "Rose"
total_price = 50.75
date_of_birth = "1995-05-15"

## Assigning multiple values
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

## Assigning the same value to multiple variables
a = b = c = 100

print(a, b, c)

## Unpacking Values from a List:
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)  # apple
print(y)  # banana  
print(z)  # cherry

## Checking a variable's value and output
score = 85
print(score)    # 85

    ## print multiple variables in a single line

name = "Alice"
age = 30
print("Name:",name, "Age:", age) # Alice, 30

    ## '+' operator can be used to concatenate strings and variables

first_name = "John"
last_name = "Doe"
print("Full Name:", first_name +" "+ last_name) # John Doe

    ## Global Variables:

name = "Johnny"

def my_function():
    print("Welcome to community,",name)