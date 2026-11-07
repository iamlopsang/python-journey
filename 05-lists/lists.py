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

    ## 3.2 . Go to the end:
"""     If you omit the end index, it defaults to the length of the list, meaning that the slice will
        go to the end of the list.
        """
print(fruits[2:])  # Output: ['cherry', 'date', 'elderberry']

"""Note: Starts at index 2 and goes to the end of the list."""

    ## 3.3. Negative range:
"""     You can also use negative indices in slicing. The slice will start from the element at the 
start index and go up to, but not include, the element at the end index.
        """
print(fruits[-3:-1])  # Output: ['cherry', 'date']


"""4. Checking if an Item Exists in a List:

    > You can check if an item exists in a list using the 'in' keyword.
    > The 'in' keyword returns True if the item is found in the list, and False otherwise."""

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

if "cherry" in fruits:
    print("Yes, 'cherry' is in the fruits list.")  # Output: Yes, 'cherry' is in the fruits list.
else:
    print("No, 'cherry' is not in the fruits list.")

"""Example of 'not in' list check:"""

if "orange " not in fruits:
    print("No, 'orange' is not in the fruits list.")  # Output: No, 'orange' is not in the fruits list. 


"""5. Changing List Items:

    > Lists are mutable, meaning that you can change their contents after they are created.
    > You can change the value of a specific item in a list by accessing it using its index and 
    assigning a new value to it.
    """

fruits = ["apple", "banana", "cherry"]

fruits[1] = "blueberry"  # Change the second item (index 1) to "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']   

    ## 5.1. Change Multiple Items:
"""     You can also change multiple items in a list by specifying a range of indices and assigning new values to that slice."""
fruits[0:2] = ["blueberry", "cranberry"]  # Change the first two items
print(fruits)  # Output: ['blueberry', 'cranberry', 'cherry']   

"""Note: The slice 0:2 includes the elements at index 0 and 1, but not the element at index 2.
 The new values replace the old values in that range.
 Index 0 is blueberry and index 1 is cranberry, so the list becomes ['blueberry', 'cranberry', 'cherry']."""

"""6. List Length:

    > You can find the number of items in a list using the len() function.
    > The len() function returns the total number of elements in the list.
    """
print(len(fruits))  # Output: 3

"""7. Adding Items to a List:
    > You can add a new item to the end of a list using the 'append()' method.
    > You can also add a new item at a specific index using the 'insert()' method.
    """
fruits = ["blueberry", "cranberry", "cherry"]
fruits.append("fig")  # Add "fig" to the end of the list
print(fruits)  # Output: ['blueberry', 'cranberry', 'cherry', 'fig']

fruits.insert(1, "grape")  # Insert "grape" at index 1
print(fruits)  # Output: ['blueberry', 'grape', 'cranberry', 'cherry', 'fig']   

## 7.1. append() method:
"""     The append() method adds a single item to the end of the list. It takes one argument, which is the item to be added.
        """
name = ["Alice", "Bob", "Charlie"]
name.append("David")  # Add "David" to the end of the list
print(name)  # Output: ['Alice', 'Bob', 'Charlie', 'David']

## 7.2. insert() method:
"""     The insert() method allows you to add an item at a specific index in the list. 
It takes two arguments: the index where the item should be inserted and the item itself.
        """
colors = ["red", "green", "blue"]
colors.insert(1, "yellow")  # Insert "yellow" at index 1
print(colors)  # Output: ['red', 'yellow', 'green', 'blue']

## 7.3. extend() method:
"""     The extend() method allows you to add multiple items to the end of a list. 
It takes an iterable (like another list) as an argument and adds each element of that iterable to 
the end of the list.
        """

fruits = ["apple", "banana", "cherry"]
more_fruits = ["date", "elderberry", "fig"]
fruits.extend(more_fruits)  # Add all items from more_fruits to fruits
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

"""Note: extends() adds the individual elements rather than making the second list one item."""

"""8. Removing Items from a List:
    > You can remove an item from a list using the 'remove()' method, which removes the first occurrence of the specified value.
    > You can also use the 'pop()' method to remove an item at a specific index, or the 'del' statement to remove an item at a specific index or delete the entire list.
    > The 'clear()' method removes all items from the list, leaving it empty."""

## 8.1. remove() method:
"""     The remove() method removes the first occurrence of a specified value from the list.
        """

colors = ["red", "green", "blue", "green"]
colors.remove("green")  # Remove the first occurrence of "green"
print(colors)  # Output: ['red', 'blue', 'green']

"""Note:  If the value appears multiple times in the list, only the first occurrence will be removed.
 If the value is not found, a ValueError will be raised."""

## 8.2. pop() method:
"""     The pop() method removes and returns the item at the specified index.
        If no index is specified, it removes and returns the last item in the list.
        """

names = ["Alice", "Bob", "Charlie", "David"]
removed_name = names.pop(1)  # Remove the item at index 1 ("Bob")
print(removed_name)  # Output: Bob
print(names)  # Output: ['Alice', 'Charlie', 'David']

"""Note: If you call pop() without an index, it will remove and return the last item in the list."""

## 8.3. del statement:
"""     The del statement can be used to remove an item at a specific index or delete the entire list.
        """

fruits = ["apple", "banana", "cherry", "date"]
del fruits[1]  # Remove the item at index 1 ("banana")
print(fruits)  # Output: ['apple', 'cherry', 'date']

"""Note: You can also use del to delete the entire list by using del list_name."""


## 8.4. clear() method:
"""     The clear() method removes all items from the list, leaving it empty.
        """
name = ["Alice", "Bob", "Charlie"]
name.clear()  # Remove all items from the list
print(name)  # Output: []
