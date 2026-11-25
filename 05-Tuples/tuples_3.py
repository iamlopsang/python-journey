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

