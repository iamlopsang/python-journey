"""12. Tuple Immutability (Why Tuples Cannot Be Changed):

1. What is Tuple Immutability?

Tuple immutability means that once a tuple is created, its items cannot be changed, added, or removed.
In Python, tuples are called immutable data types because their contents cannot be modified after creation.
For example, you can access tuple items, loop through them, and slice them, but you cannot directly replace an item with a new value.

## Trying to Change a Tuple Item:

    You cannot change an existing tuple item using its index.
"""

##Example:

# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Trying to change an item
fruits[1] = "orange"

# Displaying the tuple
print(fruits)

## output:

# TypeError: 'tuple' object does not support item assignment

"""Explanation:
- fruits[1] refers to "banana".
- We are trying to replace "banana" with "orange".
- However, tuples do not support item assignment.
- Python raises a TypeError because tuple items cannot be changed.
The print() statement does not execute because the error stops the program."""

"""12.1 Tuples Cannot Be Changed Using Indexing:

Let's compare a list and a tuple."""

## Example:

# Creating a list
my_list = ["apple", "banana", "cherry"]

# Changing a list item
my_list[1] = "orange"

print(my_list)

# Creating a tuple
my_tuple = ("apple", "banana", "cherry")

# Trying to change a tuple item
my_tuple[1] = "orange"

print(my_tuple)

## output:

# ['apple', 'orange', 'cherry']
# TypeError: 'tuple' object does not support item assignment

"""Explanation:
- Lists are mutable, so my_list[1] = "orange" works.
- Tuples are immutable, so my_tuple[1] = "orange" raises an error."""

"""12.1 Tuples Cannot Be Added to Directly:

You cannot use the append() method to add an item to a tuple because tuples do not have an append() method."""

##  Example:

# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Trying to add an item
fruits.append("orange")

## output:

# AttributeError: 'tuple' object has no attribute 'append'

"""Explanation:

The append() method is used to add items to a list. Tuples do not support this method because they are immutable."""

