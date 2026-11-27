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

"""17 : Asterisk * in Tuple Unpacking:

The asterisk * in tuple unpacking collects multiple remaining items into a list.
It is useful when you don't know how many items a tuple contains, or when you want to assign some items to separate variables and collect the rest together.
"""

##  Example 1: Collecting Remaining Items

# Creating a tuple
numbers = (10, 20, 30, 40, 50)

# Unpacking with asterisk
first, *rest = numbers

print(first)
print(rest)

## output:

10
[20, 30, 40, 50]

"""Explanation:

- first receives the first item, 10.
- *rest collects all remaining items into a list.
Notice that rest is a list, not a tuple."""

## Example 2:Collecting Items in the Middle

# Creating a tuple
numbers = (10, 20, 30, 40, 50)

# Unpacking
first, *middle, last = numbers

print(first)
print(middle)
print(last)

## output:

10
[20, 30, 40]
50

"""Explanation:

- first receives the first item.
- *middle collects all items between the first and last.
- last receives the last item.
"""

##  Example 3: Collecting Items at the Beginning

numbers = (10, 20, 30, 40, 50)

*beginning, last = numbers

print(beginning)
print(last)

## output:

[10, 20, 30, 40]
50

"""Note:

Important points
- Only one starred variable is allowed in a single unpacking assignment.
- The starred variable always collects the remaining items into a list.
- It can be placed at the beginning, middle, or end.
"""