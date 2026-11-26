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

"""12.2 5. Tuples Cannot Be Removed from Directly:

You cannot use the remove() method to remove an item from a tuple."""

## Example:

# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Trying to remove an item
fruits.remove("banana")

## output:

# AttributeError: 'tuple' object has no attribute 'remove'

"""Explanation:

The remove() method belongs to lists. Since tuples cannot be modified, Python does not provide this method for tuples."""

"""12.3 Important Exception: Tuples Can Contain Mutable Objects:

Although tuples themselves are immutable, they can contain mutable objects such as lists.
The tuple cannot change which objects it contains, but a mutable object inside it can still be modified."""

## Example:

# Creating a tuple containing a list
my_tuple = ("apple", [10, 20, 30], "banana")

# Changing an item inside the list
my_tuple[1][0] = 100

# Displaying the tuple
print(my_tuple)

## output:

('apple', [100, 20, 30], 'banana')

"""Explanation:
- my_tuple[1] accesses the list [10, 20, 30].
- my_tuple[1][0] accesses the first item inside that list.
- We change the list's first item from 10 to 100.
- The list is mutable, so this change is allowed."""

"""13. Changing Tuple Values (Workaround):

    ## Can We Change Tuple Values?

    Tuples are immutable, which means we cannot directly change, add, or remove their items.
    However, Python allows us to create a new tuple with modified values using a workaround.

    There are two common ways to do this:
    1. Convert the tuple into a list, modify it, and convert it back into a tuple.
    2. Create a new tuple by joining the required values.

    ## 13.1 Changing Tuple Values by Converting to a List:

    A list is mutable, so we can change its items after creating it.
    We can convert a tuple into a list using the list() function, modify the list, and then convert 
    it back into a tuple using the tuple() function.
"""

## Example:

# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Converting the tuple into a list
my_list = list(fruits)

# Changing an item in the list
my_list[1] = "orange"

# Converting the list back into a tuple
fruits = tuple(my_list)

# Displaying the modified tuple
print(fruits)

## output:

('apple', 'orange', 'cherry')

"""Explanation:
1. fruits stores the original tuple.
2. list(fruits) converts the tuple into a list.
3. my_list[1] = "orange" changes the second item.
4. tuple(my_list) converts the modified list back into a tuple.
5. The new tuple is assigned to the variable fruits."""

"""13.1 Changing Tuple Values by Creating a New Tuple:

You can also create a new tuple using the existing tuple's items and the values you want to change."""

## Example:

# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Creating a new tuple with a changed value
fruits = fruits[0:1] + ("orange",) + fruits[2:]

# Displaying the new tuple
print(fruits)

## output:

('apple', 'orange', 'cherry')

"""Explanation:
- fruits[0:1] retrieves the first item: ("apple",).
- ("orange",) creates a tuple containing one item.
- fruits[2:] retrieves the items from index 2 to the end: ("cherry",).
- The + operator joins these tuples together.
- The new tuple is assigned to fruits."""

"""14. Adding Items to a Tuple:

    ## Can We Add Items to a Tuple?

    Tuples are immutable, which means we cannot directly add new items to an existing tuple.
    Unlike lists, tuples do not have an append() or extend() method.

    However, we can add items by creating a new tuple using tuple concatenation (+) or by converting the tuple into a list.

    2. Adding an Item Using Tuple Concatenation (+)

    The + operator is used to join two or more tuples together.
    To add a single item, we first need to create a tuple containing that item."""