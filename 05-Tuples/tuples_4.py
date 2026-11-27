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