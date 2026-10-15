        ## Python Variables  ##

# Creating variables
name = "Alex"
age = 25

print(name)     #Alex
print(age)      #25

# Variable naming rules
# 1. Variable names must start with a letter or an underscore (_).
# 2. Variable names cannot contain spaces.
# 3. Variable names are case-sensitive.

# Valid naming examples of variables:

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



# Assigning multiple values
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

# Assigning the same value to multiple variables
a = b = c = 100

print(a, b, c)

# Checking a variable's value
score = 85
print(score)