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

"""1. List Items and Indexing:

    > Indexing: Each element in a list has an index, starting from 0 for the first element.
    > Accessing List Items: You can access individual elements in a list using their index. 
    The syntax for accessing an element is list[index].
    """

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

"""2. Negative Indexing:

    > Negative indexing allows you to access elements from the end of the list. 
    The last element has an index of -1, the second last has an index of -2, and so on.
    """
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[-1])  # Output: elderberry
print(fruits[-2])  # Output: date
print(fruits[-3])  # Output: cherry

"""3. Range of Lists Items (Slicing):
    > Slicing allows you to access a range of elements in a list. 
    The syntax for slicing is list[start:end], where start is the index of the first element to include, 
    and end is the index of the first element to exclude.
    > You can also use list[start:end:step] to specify a step value, which determines the interval
      between elements.
    > If you omit the start index, it defaults to 0. If you omit the end index, it defaults to the 
    length of the list."""

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[1:4])     # Output: ['banana', 'cherry',
print(fruits[:3])      # Output: ['apple', 'banana', 'cherry']
print(fruits[2:])      # Output: ['cherry', 'date', 'elderberry']
print(fruits[::2])     # Output: ['apple', 'cherry', 'elderberry']
print(fruits[1:4:2])   # Output: ['banana', 'date']
print(fruits[-1:-3])   # Output: ['elderberry', 'date', 'cherry']

    ## 3.1. Start from the beginning:
"""     If you omit the start index, it defaults to 0, meaning that the slice will start from
        the beginning of the list.
        """

print(fruits[:3])  # Output: ['apple', 'banana', 'cherry']

"""Note: Starts at the beginning of the list and goes up to, but does not include, the element at index 3."""
