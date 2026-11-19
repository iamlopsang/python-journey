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