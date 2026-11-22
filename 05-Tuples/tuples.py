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