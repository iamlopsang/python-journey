    ## TUPLES IN PYTHON ##

"""A tuple is another collection used to store multiple values in one variable.
Tuples are:
    > Ordered,
    > Unchangeable (immutable),
    > Allow duplicate values,
    > Indexed,
    > Written using round brackets()
    
    Example:
    fruits = ("apple", "banana", "cherry")
    print(fruits)
    
    output:
    ('apple', 'banana', 'cherry')
 
    """
##  1.Creating a Tuple:

"""To create a tuple, write multiple items inside round brackets (), separated by commas.

    Syntax:
    
    tuple_name = (item1, item2, item3)
    """

# Creating a tuple of fruits
fruits = ("apple", "banana", "cherry")

# Displaying the tuple
print(fruits)

## output:

('apple', 'banana', 'cherry')

"""Explanation:
> fruits is the name of the tuple.
> Round brackets () indicate that we are creating a tuple.
> The items "apple", "banana", and "cherry" are stored inside the tuple.
> print(fruits) displays all the items in the tuple.
"""

## 2.Creating a tuple without round brackets:

"""In Python, you can also create a tuple without using round brackets. This is called tuple packing.
"""

# Example:

# Creating a tuple without round brackets
fruits = "apple", "banana", "cherry"

# Displaying the tuple
print(fruits)

## output:

('apple', 'banana', 'cherry')

"""Explanation:
Python automatically recognizes multiple comma-separated values as a tuple, even without round brackets.
However, using round brackets is recommended because it makes your code easier to read.
"""

## 3.Creating a Tuple with Different Data Types:

"""A tuple can store different types of data, such as strings, integers, floats, and Boolean values."""

## Example:

# Creating a tuple with different data types
my_tuple = ("Ram", 22, 3.27, True)

# Displaying the tuple
print(my_tuple)

## output:

('Ram', 22, 3.27, True)

"""Explanation:

- "Ram" is a string.
- 22 is an integer.
- 3.27 is a float.
- True is a Boolean value.
Python allows different data types to be stored together in one tuple.
"""

## 4.Creating an empty tuple:

"""An empty tuple is a tuple that contains no items."""

# Example:

# Creating an empty tuple
my_tuple = ()

# Displaying the tuple
print(my_tuple)

# Checking the data type
print(type(my_tuple))

## output:

# ()
# <class 'tuple'>

"""Explanation:

> () creates an empty tuple.
> type() checks the data type of a variable.
> Python returns <class 'tuple'>, confirming that it is a tuple.
"""

## 5.Creating a Tuple with One Item:

"""When creating a tuple with only one item, you must include a comma , after the item."""

## Example:

# Creating a tuple with one item
my_tuple = ("apple",)

# Displaying the tuple
print(my_tuple)

# Checking the data type
print(type(my_tuple))

## output:

# ('apple',)
# <class 'tuple'>

"""
Explanation:

> The comma tells Python that we are creating a tuple.
> Without the comma, Python considers the brackets as ordinary grouping parentheses.
"""

## Example without a comma:

# Creating a variable with one string
my_tuple = ("apple")

# Displaying the value
print(my_tuple)

# Checking the data type
print(type(my_tuple))

## output:

# apple
# <class 'str'>

"""Accessing Tuple Items (Indexing):

1. What is Tuple Indexing?
Indexing is used to access individual items from a tuple using their position (index number).

In Python, indexing starts from 0, not 1.

For example, the first item has index 0, the second item has index 1, and so on.
"""

## 6.Tuples Items and Indexing:

"""Tuples use indexes just like lists."""

fruits = ("apple", "banana", "cherry")
print(fruits[0])
print(fruits[1])

## output:
# apple
# banana

""" 6.1 Positive Indexing:

Positive indexing means accessing tuple items using index numbers starting from 0 (left to right).
"""

## Example:

# Creating a tuple of fruits
fruits = ("apple", "banana", "cherry", "orange")

# Accessing tuple items using positive indexing
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

## output:

# apple
# banana
# cherry
# orange

""" 6.2 Negative Indexing:

Negative indexing is used to access tuple items starting from the end (right to left). In Python, the 
last item has an index of -1, the second-last item has an index of -2, and so on.
"""
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

## output:

# cherry

"""6.3 Accessing Items Using Variables:

You can also store an index number in a variable and use it to access a tupe item.
"""

## Example:

# Creating a tuple
fruits = ("apple", "banana", "cherry", "orange")

# Storing an index number
index = 2

# Accessing an item using the index variable
print(fruits[index])

## output:

# cherry

"""
Explanation:
- index = 2 stores the index number 2.
- fruits[index] accesses the item at index 2.
- The item at index 2 is "cherry".
"""

""" 6.4 Accessing Items Using Negative Indexing:
Negative indexing allows you to access tuple items starting from the end (right to left).

In negative indexing, the last item has index -1, the second-last item has index -2, and so on.
"""

# Creating a tuple of fruits
fruits = ("apple", "banana", "cherry", "orange")

# Accessing items using negative indexing
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])

## output:

# orange
# cherry
# banana
# apple

"""
Explanation:
- fruits[-1] accesses the last item "orange".
- fruits[-2] accesses the second-last item "cherry".
- fruits[-3] accesses "banana".
- fruits[-4] accesses the first item "apple".
"""

"""6.5 Indexing with Different Data Types:
You can access items from a tuple containing different data types using their index positions.
"""
# Creating a tuple with different data types
student = ("Mark", 22, 3.27, True)

# Accessing individual items
print(student[0])
print(student[1])
print(student[2])
print(student[3])

## output:

# Mark
# 22
# 3.27
# True

"""6.6 Accessing an Item with an Invalid Index:
If you try to access an item using an index that does not exist, Python raises an IndexError."""

## Example:

# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Accessing an invalid index
print(fruits[5])

## output:

# IndexError: tuple index out of range