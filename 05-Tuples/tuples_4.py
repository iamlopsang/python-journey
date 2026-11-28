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

"""18. Joining Tuples (+):

Joining tuples means combining two or more tuples into a new tuple using the + operator.
The original tuples remain unchanged because tuples are immutable.

     Syntax:
          new_tuple = tuple1 + tuple2
          """

## Example 1 :Joining Two Tuples:

# Creating two tuples
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# Joining tuples
result = tuple1 + tuple2

print(result)

## output:

(10, 20, 30, 40, 50, 60)

"""Explanation:

The + operator places the items of tuple2 after the items of tuple1, creating a new tuple."""

## Example 2: Joining three tuples

# Creating three tuples
a = ("apple", "banana")
b = ("orange", "grape")
c = ("mango", "kiwi")

# Joining tuples
fruits = a + b + c

print(fruits)

## output:

('apple', 'banana', 'orange', 'grape', 'mango', 'kiwi')

"""Note: You can only use + to join compatible sequence types, such as tuple with tuple."""
# Example of it:

numbers = (10, 20, 30)

result = numbers + (40,)

print(result)

## output:

(10, 20, 30, 40)

# Remember: (40,) is a single-item tuple. (40) is just an integer inside parentheses.

