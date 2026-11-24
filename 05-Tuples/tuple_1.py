"""7. Slicing in Tuple:

Tuple slicing is used to access a range of items from a tuple by specifying their index positions.

Instead of accessing one item at a time, slicing allows you to retrieve multiple items from a tuple.

Slicing uses square brackets [] with a colon :.

    Syntax:

    tuple_name[start:end]

    Explanation:

    > start: The index where slicing begins (included).
    > end: The index where slicing stops (excluded).

"""

## Example:

# Creating a tuple
fruits = ("apple", "banana", "cherry", "orange", "mango")

# Accessing a range of items
print(fruits[1:4])

## output:

('banana', 'cherry', 'orange')

"""Explantion:

> fruits[1:4] starts slicing from index 1.
> It includes "banana", "cherry", and "orange".
> It stops before index 4, so "mango" is not included.
"""

""" 7.1 Slicing from the beginning:

You can leave the start index empty to access items from the beginning of the tuple.
"""
## Example:

# Creating a tuple
fruits = ("apple", "banana", "cherry", "orange", "mango")

# Slicing from the beginning
print(fruits[:3])

## output:

('apple', 'banana', 'cherry')

"""Explanation:

> fruits[:3] starts from the beginning (index 0).
> It accesses items up to index 2.
> It stops before index 3.
"""

"""7.2 Slicing to the end:

You can leave the end index empty to access items from a particular index to the end of the tuple.
"""

## Example:

# Creating a tuple
fruits = ("apple", "banana", "cherry", "orange", "mango")

# Slicing to the end
print(fruits[2:])

## output:

('cherry', 'orange', 'mango')

"""Explanation:

> fruits[2:] starts from index 2.
> It retrieves all items from "cherry" to the end of the tuple.
"""

"""7.3 Using negative Indexing in  Slicing:

You can also use negative indexes to slice a tuple from the end.
"""

## Example:

# Creating a tuple
fruits = ("apple", "banana", "cherry", "orange", "mango")

# Slicing using negative indexing
print(fruits[-4:-1])

## output:

('banana', 'cherry', 'orange')

"""Explanation:

> fruits[-4] starts from "banana".
> fruits[-1] refers to "mango", but the end index is excluded.
> Therefore, the result contains "banana", "cherry", and "orange"."""

"""7.4 Using the Step Value in Slicing of Tuple:

You can use a third value called step to control how many positions Python skips when retrieving tuple items.

    Syntax:

        tuple_name[start:end:step]

    Explantion:

    > start: Starting index.
    > end: Ending index (excluded).
    > step: Number of positions to move between selected items.
"""
## Example:

# Creating a tuple
numbers = (10, 20, 30, 40, 50, 60, 70)

# Accessing items with a step of 2
print(numbers[0:7:2])

## output:

(10, 30, 50, 70)

"""Explanation:

> numbers[0:7:2] starts from index 0.
> It moves forward by 2 positions each time.
> Python selects the items at indexes 0, 2, 4, and 6.
> The ending index 7 is excluded.
"""

"""7.5 Reversing a Tuple Using Slicing:

You can reverse the order of tuple items using a negative step value of -1.
"""

## Example:

# Creating a tuple
numbers = (10, 20, 30, 40, 50)

# Reversing the tuple
print(numbers[::-1])

## output:

(50, 40, 30, 20, 10)

"""Explanation:

> numbers[::-1] leaves the start and end indexes empty.
> The step value -1 tells Python to move backward.
> Python retrieves all items in reverse order.
"""

"""8. Checking if an Item Exists in a Tuple (in and not in):

What is Tuple Membership?
Tuple membership is used to check whether a particular item exists or does not exist in a tuple.

Python provides two membership operators:
- in: Checks whether an item exists in a tuple.
- not in: Checks whether an item does not exist in a tuple.
Both operators return a Boolean value: True or False.
"""

""" 8.1 Using the in Operator:

The in operator checks whether a specified item exists in a tuple.
It returns True if the item exists and False if it does not. 

    Syntax:

    item in tuple_name
"""

## Example:

# Creating a tuple of fruits
fruits = ("apple", "banana", "cherry", "orange")

# Checking whether an item exists
print("banana" in fruits)
print("mango" in fruits)

## output:

True
False

"""
Explanation:

- "banana" in fruits checks whether "banana" exists in the tuple. Since it exists, Python returns True.
- "mango" in fruits checks whether "mango" exists in the tuple. Since it does not exist, Python returns False.
"""

"""8.2 Using the not in Operator:

The not in operator checks whether a specified item does not exist in a tuple.
It returns True if the item is absent and False if it exists.

    Syntax:

    item not in tuple_name
"""

## Example:

# Creating a tuple of animals
animals = ("cat", "dog", "lion", "tiger")

# Checking whether an item is absent
print("elephant" not in animals)
print("lion" not in animals)

## output:

True
False

"""
Explanation:
- "elephant" not in animals returns True because elephant is not present in the tuple.
- "lion" not in animals returns False because lion already exists in the tuple.
"""

"""8.3 Using Membership Operators with Conditional Statements:

You can also use in and not in inside if-else statements to execute code based on whether an item exists in a tuple.
"""

## Example:

# Creating a tuple of available courses
courses = ("Python", "SQL", "Java", "Excel")

# Checking whether a course is available
if "Python" in courses:
    print("Python course is available.")
else:
    print("Python course is not available.")

## output:

# Python course is available.

"""
Explanation:
- The if statement checks whether "Python" exists in the courses tuple.
- Since Python exists, the condition returns True.
- Therefore, the code inside the if block is executed.
- The else block is skipped.
"""

"""9. Length of a Tuple (len()):
1. What is the len() Function?
The len() function is a built-in Python function used to find the total number of items in a tuple.

It counts every item in the tuple, including duplicate values and items with different data types.

    Syntax:

    len(tuple_name)
"""

    ## Example- finding the length of the tuple

# Creating a tuple of fruits
fruits = ("apple", "banana", "cherry", "orange")

# Finding the length of the tuple
print(len(fruits))

## output:
4

"""Explanation:
- The fruits tuple contains four items.
- len(fruits) counts the total number of items.
- Therefore, Python returns 4.
"""

"""
9.1. Finding the Length of a Tuple with Duplicate Items:

The len() function counts duplicate items separately.
"""

## Example:

# Creating a tuple with duplicate items
numbers = (10, 20, 20, 30, 40, 40)

# Finding the length
print(len(numbers))

## output:
6

"""Explanation:
> Even though some values are repeated, Python counts every occurrence as a separate item.
> Therefore, the total number of items is 6.
"""

"""9.2 Finding the Length of an Empty Tuple:

An empty tuple contains no items. Therefore, its length is 0.
"""
## Example:

# Creating an empty tuple
my_tuple = ()

# Finding the length
print(len(my_tuple))

## output:
0

"""9.3  Using len() with Conditional Statements:

You can use the len() function with conditional statements to check whether a tuple contains items or is empty.
"""

## Example:

# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Checking whether the tuple is empty
if len(fruits) > 0:
    print("The tuple is not empty.")
else:
    print("The tuple is empty.")

## output:

# The tuple is not empty.

"""
Explanation:
- len(fruits) returns 3.
- Python checks whether 3 > 0.
- Since the condition is True, the if block executes.
- Therefore, it prints "The tuple is not empty.".
"""

