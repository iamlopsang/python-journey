## Python Chapter 04 — Lists

    ## About This Chapter:

    This chapter covers Python lists, one of the built-in data types used to store multiple items in a single variable. It explores list creation, accessing and modifying elements, built-in list methods, and different ways to organize and manipulate list data.

 ##   Topics Covered:

    1. Creating Lists (lists.py)

    > Understanding lists and their characteristics,
    > Creating lists using square brackets [],
    > Creating empty lists,
    > Creating lists with different data types,
    > Creating lists containing other lists,
    > Understanding ordered, mutable, and duplicate elements,
    > Creating lists using the list() constructor.

    2. Accessing List Items and Indexing

    > Understanding list indexing,
    > Accessing elements using positive indexing,
    > Accessing elements using negative indexing,
    > Retrieving items from different positions in a list.

    3. List Slicing

    > Extracting a range of elements using slicing,
    > Using the start:end slicing syntax,
    > Specifying a step value using start:end:step,
    > Slicing from the beginning of a list,
    > Slicing to the end of a list,
    > Using negative indexing in slices,
    > Reversing a list using slicing.

    4. Checking Items in a List

    > Checking whether an item exists using the in operator,
    > Checking whether an item does not exist using not in,
    > Using membership checks in if statements,
    > Understanding the Boolean results of membership checks.

    5. Changing List Items

    > Modifying individual elements using their indexes,
    > Replacing multiple elements using slicing,
    > Understanding how list mutability allows elements to be changed.

    6. Finding List Length

    > Finding the number of elements using len(),
    > Checking the length of empty and non-empty lists,
    > Understanding how duplicate elements contribute to list length.

    7. Adding Items to a List

    List Methods:

    > append() — adds a single item to the end of a list,
    > insert() — adds an item at a specified index,
    > extend() — adds elements from another iterable to the end of a list.

    8. Removing Items from a List

    List Methods and Statements:

    > remove() — removes the first occurrence of a specified value,
    > pop() — removes and returns an item at a specified index, or the last item by default,
    > del — removes an item at a specified index or deletes the entire list,
    > clear() — removes all items from a list.

    9. Looping Through a List

    > Iterating through list elements using a for loop,
    > Accessing list elements using a while loop and indexing,
    > Looping through indexes using range() and len(),
    > Displaying individual list elements,
    > Performing operations on list elements inside loops.

    10. Sorting a List

    > Sorting elements in ascending order using sort(),
    > Sorting elements in descending order using reverse=True,
    > Sorting strings alphabetically,
    > Using sorted() to create a new sorted list,
    > Understanding the difference between sort() and sorted().

    11. Reversing a List

    > Reversing the order of elements using reverse(),
    > Reversing a list using slicing [::-1],
    > Understanding the difference between modifying the original list and creating a reversed copy.

    12. Copying a List

    > Creating a copy using copy(),
    > Creating a copy using the list() constructor,
    > Understanding the difference between an original list and a copied list,
    > Modifying copied lists independently,
    > Understanding shallow copies.

    13. Joining Lists

    > Combining two or more lists using the + operator,
    > Joining lists using extend(),
    > Understanding the difference between + and extend(),
    > Combining lists containing duplicate values,
    > Finding the total number of elements after joining lists.

    14. Nested Lists

    > Understanding lists inside other lists,
    > Creating nested lists,
    > Accessing inner lists using indexing,
    > Accessing individual elements inside nested lists using multiple indexes.

    15. List Comprehensions

    > Understanding list comprehensions,
    > Creating new lists from existing iterables,
    > Using the basic list comprehension syntax,
    > Performing expressions on list elements,
    > Filtering elements using conditions in list comprehensions.

    List Comprehension Syntax:

    [expression for item in iterable if condition]

 ##   Exercises (exercises.py):

    > Practising list creation and working with different data types,
    > Accessing elements using positive and negative indexing,
    > Extracting elements using list slicing,
    > Checking whether items exist in a list,
    > Modifying individual and multiple list elements,
    > Finding the length of a list using len(),
    > Adding elements using append(), insert(), and extend(),
    > Removing elements using remove(), pop(), del, and clear(),
    > Looping through lists using for and while loops,
    > Sorting and reversing lists,
    > Creating and modifying copies of lists,
    > Joining multiple lists using + and extend(),
    > Working with nested lists and list comprehensions.

 ##  What I Learned:

   > Creating lists and understanding their characteristics, including ordering, mutability, and duplicate elements.
   > Accessing, modifying, and extracting list elements using indexing and slicing.
   > Checking list contents using membership operators.
   > Adding and removing elements using built-in list methods.
   > Finding list length and performing operations through loops.
   > Sorting and reversing lists using different methods.
   > Creating independent list copies and understanding their behavior.
   > Combining multiple lists using the + operator and extend().
   > Understanding nested lists and creating new lists using list comprehensions.

##   Purpose:

      To develop a strong foundation in Python list operations and data manipulation by understanding list characteristics, practising 
      built-in methods, and applying different techniques to work with collections of data.

## Folder Structure:

      04-lists/
      │
      ├── README.md
      ├── lists.py
      └── exercises.py