    ##  LISTS IN PYTHON ##

"""A list is a collection of items in a particular order. In Python, lists are mutable, meaning that 
their contents can be changed after they are created. Lists can contain elements of different data types,
 including other lists.
 
 Lists are:
 - Ordered: The order of elements in a list is preserved.
 - Mutable: The elements of a list can be changed after the list is created.
 - Heterogeneous: A list can contain elements of different data types.
 - Allow duplicates: Lists can contain duplicate elements.
 - Indexed: Each element in a list has an index, starting from 0 for the first element.
 - Written with square brackets: Lists are defined using square brackets [].

    Lists are one of the 4 built-in data types in Python used to store collections of data,
      the other 3 are 
      > Tuple, 
      > Set, and 
      > Dictionary, 
      all with different qualities and usage.
 """

"""## Creating a List:"""

fruits = ["apple", "banana", "cherry"]
print(fruits)   # Output: ['apple', 'banana', 'cherry']

"""A list can contain elements of different data types, including other lists:"""

student = ["John", 25, 3.5, ["Math", "Science"]]
print(student)  # Output: ['John', 25, 3.5, ['Math', 'Science']]

"""Empty lists can be created using empty square brackets or the list() constructor:"""

empty_list1 = []
print(empty_list1)  # Output: []

"""1. List Indexing and Slicing:

    > Indexing: Each element in a list has an index, starting from 0 for the first element.
    > Slicing: You can access a range of elements in a list using slicing.
    """

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry


"""Slicing allows you to access a range of elements in a list. The syntax for slicing is list[start:end],"""
print(fruits[1:4])  # Output: ['banana', 'cherry', 'date']
print(fruits[:3])   # Output: ['apple', 'banana', 'cherry']
print(fruits[3:5])  # Output: ['date', 'elderberry']

