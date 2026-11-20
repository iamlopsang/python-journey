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




## 1.Tuples Items and Indexing:

"""Tuples use indexes just like lists."""

fruits = ("apple", "banana", "cherry")
print(fruits[0])
print(fruits[1])

## output:
# apple
# banana

## 2.Negative Indexing:

""""""