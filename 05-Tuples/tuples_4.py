"""16 Tuple Unpacking:

Tuple unpacking is assigning the items of a tuple to multiple variables in a single statement.
Each variable receives one item from the tuple according to its position.

     Syntax:

     variable1, variable2, variable3 = tuple_name
"""

## Example:Basic Tuple unpacking

# Creating a tuple
student = ("Leon", 22, 3.27)

# Unpacking tuple items
name, age, gpa = student

# Displaying the variables
print(name)
print(age)
print(gpa)

## output:

# Leon
# 22
# 3.27


"""Explanation:

The tuple contains three items:

Tuple item	Variable
"Lopsang"	->    name
22	        ->    age
3.27	    ->    gpa

Python assigns each item to the variable in the same position."""

##  Example 2: Unpacking a Tuple of Numbers

# Creating a tuple
numbers = (10, 20, 30)

# Unpacking
a, b, c = numbers

print(a)
print(b)
print(c)

## output:

10
20
30

"""Important: The number of variables must match
Normally, the number of variables must be equal to the number of tuple items."""

## Example:

numbers = (10, 20, 30)

a, b = numbers

## output:

# ValueError: too many values to unpack

"""There are three items but only two variables.

Similarly, if there are more variables than items, Python raises:"""

## ValueError: not enough values to unpack