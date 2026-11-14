"""Python Lists Exercises
This file contains a series of exercises to help you practice working with Python lists."""

""" Creating Lists """ 
# 1. Create a list containing five different fruits and print the list.

# Creating a list of five different fruits
fruits = ["apple", "banana", "orange", "cherry", "melon"]

# Printing the complete list
print(fruits)

# output:
['apple', 'banana', 'orange', 'cherry', 'melon']

# 2. Create a list containing five integer numbers.

# Creating a list of five integers
numbers = [1, 2, 3, 4, 6]

# Printing the list
print(numbers)

# output:
[1, 2, 3, 4, 6]

# 3. Create a list containing your name, age, GPA, and student status.

# Creating a list with different data types
student = ["Leon", 26, 3.89, "Active"]

# Printing student information
print(student)

# output:
['Leon', 26, 3.89, 'Active']

# 4. Create an empty list and print it.

# Creating an empty list
fruits = []

# Printing the empty list
print(fruits)

# output:   
[]

# 5. Create a list containing both integers and strings.

# Creating a list containing integers and strings
friends = [6, 7, "hello", 9, "hi"]

# Printing the list
print(friends)

# output:
[6, 7, 'hello', 9, 'hi']

# 6. Create a list containing five different student names. Print each item using print().

# Creating a list of five student names
students = ["Ram", "Shyan", "Laxmi", "Sita", "Radha"]

# Printing each item using its index
print(students[0])  # Prints Ram
print(students[1])  # Prints Shyan
print(students[2])  # Prints Laxmi
print(students[3])  # Prints Sita
print(students[4])  # Prints Radha

# output:
# Ram
# Shyan
# Laxmi
# Sita
# Radha

# 7. Create a list containing duplicate values and display it.

# Creating a list containing duplicate values

color = ["red", "white", "gold", "red", "blue"]

# Printing the list
print(color)

# output:
['red', 'white', 'gold', 'red', 'blue']

"""Note: Lists allow duplicate values. Here, "red" appears twice."""

# 8. Create a list containing three different data types: string, integer, and float.

# Creating a list with string, integer, and float values

customer = ["Kathmandu", 3345, 456.89]

# Printing the list
print(customer)

# output:
['Kathmandu', 3345, 456.89]

# 9. Create two separate lists: one containing five even numbers and another containing five odd numbers.

# Creating a list of five even numbers
even = [2, 4, 6, 8, 10]

# Creating a list of five odd numbers
odd = [1, 3, 5, 7, 9]

# Printing both lists
print(even)
print(odd)

# output:
[2, 4, 6, 8, 10]
[1, 3, 5, 7, 9]

# 10. Create a list containing the names of five programming languages and print the total list.

# Creating a list of five programming languages
language = ["python", "c", "c++", "java", "js"]

# Printing the complete list
print(language)

# Counting the total number of items
total_list = len(language)

# Printing the total count
print(total_list)

# output:
['python', 'c', 'c++', 'java', 'js']
5

""" 2. Accessing List Items"""

# 1. Create a list of five fruits and print the first item.

# Creating a list of five fruits
fruits = ["apple", "banana", "orange", "cherry", "melon"]

# Accessing the first item using index 0
print(fruits[0])

# output:
# apple

# 2. Create a list of five countries and print the third item.

# Creating a list of five countries
countries = ["Nepal", "Bhutan", "China", "Maldives", "UK"]

# Accessing the third item using index 2
print(countries[2])

# output:
# China

# 3. Create a list of six numbers and print the last item using positive indexing.

# Creating a list of six numbers
numbers = [2, 55, 67, 8, 90, 55]

# Accessing the last item using positive indexing
print(numbers[5])

# output:
# 55

# 4. Create a list of five colors and print the second-last item using negative indexing.

# Creating a list of five colors
color = ["red", "white", "gold", "orange", "blue"]

# Accessing the second-last item using negative indexing
print(color[-2])

# output:
# orange

# 5. Create a list of seven numbers and print the first, fourth, and last items.

# Creating a list of seven numbers
numbers = [2, 55, 67, 8, 90, 55, 11]

# Accessing the first item
print(numbers[0])

# Accessing the fourth item
print(numbers[3])

# Accessing the last item
print(numbers[6])

# output:
# 11

# 6. Create a list of five student names and access the name at index 2.

# Creating a list of five student names
students = ["Ram", "Shyan", "Laxmi", "Sita", "Radha"]

# Accessing the item at index 2
print(students[2])

# output:
# Laxmi

# 7. Create a list of six programming languages and print the first and last languages.

# Creating a list of six programming languages
language = ["python", "c", "c++", "java", "js", "c#"]

# Accessing the first language
print(language[0])

# Accessing the last language
print(language[5])

# output:
# c#

# 8. Create a list of five animals and access the items using negative indexes -1, -3, and -5.

# Creating a list of five animals
animals = ["cat", "dog", "tiger", "lion", "goat"]

# Accessing items using negative indexing
print(animals[-1])  # Last item
print(animals[-3])  # Third-last item
print(animals[-5])  # First item

# output:
# goat
# tiger
# cat

# 9. Create a list of eight numbers and print the items at indexes 1, 3, 5, and 7.

# Creating a list of eight numbers
numbers = [1, 3, 5, 7, 9, 44, 56, 78]

# Accessing items at indexes 1, 3, 5, and 7
print(numbers[1])
print(numbers[3])
print(numbers[5])
print(numbers[7])

# output:
# 3
# 44
# 56

# 10. Create a list containing your five favorite movies and print the second and fourth movies.

# Creating a list of five favorite movies
movies = ["Interstellar", "Inception", "Titanic", "Avatar", "The Dark Knight"]

# Accessing the second movie
print(movies[1])

# Accessing the fourth movie
print(movies[3])

# output:
# Inception
# Avatar

"""List Slicing """
# 1. Create a list of ten numbers and print the first five elements.

# Creating a list of ten numbers
numbers = [1, 5, 7, 9, 2, 5, 7, 3, 11, 15]

# Accessing the first five elements using slicing
print(numbers[0:5])

# output:
[1, 5, 7, 9, 2]

# 2. Create a list of eight fruits and print elements from index 2 to index 5.

# Creating a list of eight fruits
fruits = ["apple", "banana", "orange", "mango", "grapes", "pineapple", "watermelon", "strawberry"]

# Accessing elements from index 2 to index 5
print(fruits[2:6])

# output:
['orange', 'mango', 'grapes', 'pineapple']

# 3. Create a list of ten numbers and print the last three elements using slicing.

# Creating a list of ten numbers
numbers = [1, 5, 7, 9, 2, 5, 7, 3, 11, 15]

# Accessing the last three elements using slicing
print(numbers[7:])

# output:
[3, 11, 15]

# 4. Create a list of seven countries and print everything except the first two elements.

# Creating a list of seven countries
countries = ["Nepal", "India", "China", "Japan", "Bhutan", "Australia", "United Kingdom"]

# Printing everything except the first two elements
print(countries[2:])

# output:
# ['China', 'Japan', 'Bhutan', 'Australia', 'United Kingdom']

# 5. Create a list of ten numbers and print every second element.

# Creating a list of ten numbers
numbers = [1, 5, 7, 9, 2, 5, 7, 3, 11, 15]

# Printing every second element using step value 2
print(numbers[::2])

# output:
[1, 7, 2, 7, 11]

# 6. Create a list of eight colors and print elements from index 1 to index 6.

# Creating a list of eight colors
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black"]

# Accessing elements from index 1 to index 6
print(colors[1:7])

# output:
# ['blue', 'green', 'yellow', 'orange', 'purple', 'pink']

# 7. Create a list of ten numbers and print the elements from the beginning up to index 4.

# Creating a list of ten numbers
numbers = [1, 5, 7, 9, 2, 5, 7, 3, 11, 15]

# Printing elements from the beginning up to index 4
print(numbers[:5])

# output:
[1, 5, 7, 9, 2]

# 8. Create a list of eight fruits and extract the elements using negative slicing.

# Creating a list of eight fruits
fruits = ["apple", "banana", "orange", "mango", "grapes", "pineapple", "watermelon", "strawberry"]

# Extracting all elements using negative slicing in reverse order
print(fruits[-1:-9:-1])

# output:
"""['strawberry', 'watermelon', 'pineapple', 'grapes', 'mango', 'orange', 'banana', 'apple']"""

"""Note: 
Explanation:
- -1 = Starting from the last item.
- -9 = Ending position (excluded).
- -1 = Moves backward."""

# 9. Create a list of ten numbers and print elements from index 2 to index 8 with a step of 2.

# Creating a list of ten numbers
numbers = [1, 5, 7, 9, 2, 5, 7, 3, 11, 15]

# Printing elements from index 2 to index 8 with a step of 2
print(numbers[2:9:2])

# output:
[7, 2, 7, 11]

# 10. Create a list of six programming languages and print the last three elements using negative indexing and slicing.

# Creating a list of six programming languages
language = ["python", "c", "c++", "java", "js", "c#"]

# Printing the last three elements using negative indexing
print(language[-3:])

# output:
['java', 'js', 'c#']

"""note:
Explanation:
- -3 = Third-last item.
- Empty ending index = Continue to the end."""

""" Checking Items in a List """

# 1. Create a list of five fruits and check whether "apple" exists in it.

# Creating a list of five fruits
fruits = ["apple", "banana", "orange", "mango", "grapes"]

# Checking whether apple exists
print("apple" in fruits)

# output:
# True

# 2. Create a list of five countries and check whether "Nepal" exists.

# Creating a list of five countries
countries = ["Nepal", "Japan", "Bhutan", "Australia", "United Kingdom"]

# Checking whether Nepal exists
print("Nepal" in countries)

# output:
# True

# 3. Create a list of five numbers and check whether 10 is not present.

# Creating a list of five numbers
numbers = [1, 5, 7, 9, 2]

# Checking whether 10 is not present
print(10 not in numbers)

# output:
# True

# 4. Create a list of five colors. Use an if statement to check whether "blue" exists.

# Creating a list of five colors
color = ["red", "white", "gold", "orange", "blue"]

# Checking whether blue exists using an if statement
if "blue" in color:
    print("Blue exists in the list.")

# output:
# Blue exists in the list.

# 5. Create a list of student names and check whether a particular name exists.

# Creating a list of student names
students = ["Ram", "Shyan", "Laxmi", "Sita", "Radha"]

# Checking whether Gita exists
print("Gita" in students)

# output:
# False

# 6. Create a list of programming languages and check whether "Python" is present using in.

# Creating a list of programming languages
language = ["python", "c", "c++", "java", "js", "c#"]

# Checking whether python exists
print("python" in language)

# output:
# True

"""Note:
Python is case-sensitive. "Python" with a capital P would return False because your list contains lowercase "python"."""

# 7. Create a list of five animals and check whether "lion" is absent using not in.

# Creating a list of five animals
animals = ["cat", "dog", "tiger", "lion", "goat"]

# Checking whether lion is absent from the list
print("lion" not in animals)

# output:
# False

# 8. Create a list of numbers and check whether both 20 and 30 exist.

# Creating a list of numbers
numbers = [1, 5, 7, 9, 30]

# Checking whether both 20 and 30 exist in the list
if 20 in numbers and 30 in numbers:
    print("Both numbers exist.")
else:
    print("Both numbers do not exist.")

# output:
# Both numbers do not exist.

# 9. Create a list of fruits and check whether "mango" exists. Display an appropriate message depending on the result.

# Creating a list of fruits
fruits = ["apple", "banana", "orange", "mango", "grapes"]

# Checking whether mango exists in the list
if "mango" in fruits:
    print("Yes, mango exists in the list.")
else:
    print("Mango does not exist in the list.")

# output:
# Yes, mango exists in the list.

# 10. Ask the user to enter a fruit name and check whether that fruit exists in your predefined list.

# Creating a predefined list of fruits
fruits = ["apple", "banana", "orange", "mango", "grapes"]

# Asking the user to enter a fruit name
fruit = input("Enter a fruit name: ")

# Checking whether the entered fruit exists in the list
if fruit in fruits:
    print("Yes, the fruit exists in the list.")
else:
    print("No, the fruit does not exist in the list.")

# output:
# Enter a fruit name: mango
# Yes, the fruit exists in the list.

""" Changing List Items """

# 1. Create a list of five fruits and change the first item to "mango".

# Creating a list of five fruits
fruits = ["apple", "banana", "orange", "mango", "grapes"]

# Changing the first item to mango
fruits[0] = "mango"

# Printing the updated list
print(fruits)

# output:
# ['mango', 'banana', 'orange', 'mango', 'grapes']

# 2. Create a list of five numbers and change the third number to 100.

# Creating a list of five numbers
numbers = [1, 5, 7, 9, 2]

# Changing the third number to 100
numbers[2] = 100

# Printing the updated list
print(numbers)

# output:
# [1, 5, 100, 9, 2]

# 3. Create a list of five colors and replace the last item with "purple".

# Creating a list of five colors
color = ["red", "white", "gold", "orange", "blue"]

# Replacing the last item with purple
color[4] = "purple"

print(color)

# output:
# ['red', 'white', 'gold', 'orange', 'purple']

# 4. Create a list of six countries and change the second item to "Japan".

# Creating a list of six countries
countries = ["Nepal", "Bhutan", "China", "Australia", "United Kingdom", "Turkey"]

# Changing the second item to Japan
countries[1] = "Japan"

print(countries)

# output:
# ['Nepal', 'Japan', 'China', 'Australia', 'United Kingdom', 'Turkey']

# 5. Create a list of five student names and replace the third name with another name.

# Creating a list of five student names
students = ["Ram", "Shyan", "Laxmi", "Sita", "Radha"]

# Replacing the third name with John
students[2] = "John"

print(students)

# output:
# ['Ram', 'Shyan', 'John', 'Sita', 'Radha']

# 6. Create a list of six numbers and change the first three elements using slicing.

# Creating a list of numbers
numbers = [2, 55, 67, 8, 90, 55, 11]

# Replacing the first three elements
numbers[0:3] = [4, 7, 9]

print(numbers)

# output:
# [4, 7, 9, 8, 90, 55, 11]

# 7. Create a list of five fruits and replace the second and third elements with two different fruits.

# Creating a list of five fruits
fruits = ["apple", "banana", "orange", "cherry", "melon"]

# Replacing the second and third elements
fruits[1:3] = ["lemon", "tomato"]

print(fruits)

# output:
# ['apple', 'lemon', 'tomato', 'cherry', 'melon']

# 8. Create a list of eight numbers and replace the elements from index 2 to index 5 with [100, 200].

# Creating a list of eight numbers
numbers = [2, 55, 67, 8, 90, 55, 11, 15]

# Replacing elements from index 2 up to index 5
numbers[2:6] = [100, 200]

print(numbers)

# output:
# [2, 55, 100, 200, 11, 15]

# 9. Create a list of five programming languages and update the first and last elements.

# Creating a list of programming languages
language = ["python", "c", "c++", "java", "js"]

# Updating the first and last elements
language[0] = "php"
language[4] = "xml"

print(language)

# output:
# ['php', 'c', 'c++', 'java', 'xml']

# 10. Create a list of seven numbers and replace the middle three elements with [50, 60, 70] using slicing.

# Creating a list of seven numbers
numbers = [2, 55, 67, 8, 90, 55, 11]

# Replacing the middle three elements
numbers[2:5] = [50, 60, 70]

print(numbers)

# output:
# [2, 55, 50, 60, 70, 55, 11]


""" Finding List Length """

# 1. Create a list of five fruits and find its length.

# Creating a list of five fruits
fruits = ["apple", "banana", "orange", "cherry", "melon"]

# Finding the number of elements
print(len(fruits))

# output:
# 5

# 2. Create a list of ten numbers and display the total number of elements.

# Creating a list of ten numbers
numbers = [2, 55, 67, 8, 90, 55, 11, 78, 90, 121]

# Displaying the total number of elements
print(len(numbers))

# output:
# 10

# 3. Create an empty list and check its length.

# Creating an empty list
fruits = []

# Checking its length
print(len(fruits))

# output:
# 0

# 4. Create a list containing different data types and find its length.

# Creating a list with different data types
info = ["hello", 23, 45.0, "TRUE"]

# Finding the length
print(len(info))

# output:
# 4

# 5. Create a list of student names and display how many students are in the list.

# Creating a list of student names
students = ["Ram", "Shyan", "Laxmi", "Sita", "Radha"]

# Counting the students
print(len(students))

# output:
# 5

# 6. Create a list of seven countries and find its length.

# Creating a list of seven countries
countries = ["Nepal", "Japan", "Bhutan", "Australia", "United Kingdom", "Turkey", "Canada"]

# Finding the length
print(len(countries))

# output:
# 7

# 7. Create a list containing duplicate values and check whether duplicates affect the length.

# Creating a list with duplicate values
countries = ["Nepal", "Japan", "Bhutan", "Australia", "United Kingdom", "Turkey", "Canada", "Japan"]

# Finding the length
print(len(countries))

# output:
# 8

# 8. Ask the user to enter five numbers and store them in a list. Display the length of the list.

# Creating an empty list
numbers = []

# Asking the user to enter five numbers
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Displaying the list
print(numbers)

# Displaying the length of the list
print(len(numbers))

# output:
# [10, 20, 30, 40, 50]
# 5

# 9. Create a list of programming languages and display the total number of languages.

# Creating a list of programming languages
language = ["python", "c", "c++", "java", "js"]

# Displaying the total number of languages
print(len(language))

# output:
# 5

# 10. Create a list of ten items and check its length before and after changing one item.

# Creating a list of ten numbers
numbers = [2, 55, 67, 8, 90, 55, 11, 15, 57, 90]

# Checking the length before changing an item
print(len(numbers))

# Changing the item at index 0
numbers[0] = 100

# Printing the updated list
print(numbers)

# Checking the length after changing an item
print(len(numbers))

# output:

# 10
# [100, 55, 67, 8, 90, 55, 11, 15, 57, 90]
# 10

""" 7. Adding Items to a List """
# 1. Create a list of five fruits and add "mango" using append().

# Creating a list of five fruits
fruits = ["apple", "banana", "orange", "cherry", "melon"]

# Adding mango at the end
fruits.append("mango")

print(fruits)

# output:
# ['apple', 'banana', 'orange', 'cherry', 'melon', 'mango']

# 2. Create a list of five numbers and add 100 at the end.

# Creating a list of five numbers
numbers = [2, 55, 67, 8, 90]

# Adding 100 at the end
numbers.append(100)

print(numbers)

# output:
# [2, 55, 67, 8, 90, 100]

# 3. Create a list of colors and insert "yellow" at index 1.

# Creating a list of colors
color = ["red", "white", "gold", "orange", "blue"]

# Inserting yellow at index 1
color.insert(1, "yellow")

print(color)

# output:
# ['red', 'yellow', 'white', 'gold', 'orange', 'blue']

# 4. Create a list of student names and insert a new student at the beginning.

# Creating a list of student names
students = ["Ram", "Shyan", "Laxmi", "Sita", "Radha"]

# Inserting Rita at the beginning
students.insert(0, "Rita")

print(students)

# output:
# ['Rita', 'Ram', 'Shyan', 'Laxmi', 'Sita', 'Radha']

# 5. Create a list of five countries and add another country using append().

# Creating a list of five countries
countries = ["Nepal", "Bhutan", "China", "Japan", "Canada"]

# Adding the UK
countries.append("UK")

print(countries)

# output:
# ['Nepal', 'Bhutan', 'China', 'Japan', 'Canada', 'UK']

# 6. Create two lists of fruits and add all elements of the second list to the first using extend().

# Creating two lists of fruits
fruit1 = ["apple", "banana", "orange"]
fruit2 = ["cherry", "melon"]

# Adding fruit2 elements to fruit1
fruit1.extend(fruit2)

print(fruit1)

# output:
# ['apple', 'banana', 'orange', 'cherry', 'melon']

# 7. Create a list of numbers and insert 50 at index 3.

# Creating a list of numbers
numbers = [2, 55, 67, 8, 90]

# Inserting 50 at index 3
numbers.insert(3, 50)

print(numbers)

# output:
# [2, 55, 67, 50, 8, 90]

# 8. Create a list of programming languages and add three more languages using extend().

# Creating a list of programming languages
language = ["python", "c", "c++"]

# Adding three more languages
language.extend(["r", "java", "js"])

print(language)

# output:
# ['python', 'c', 'c++', 'r', 'java', 'js']

# 9. Create an empty list and add five numbers to it using append().

# Creating an empty list
num = []

# Adding five numbers using append()
num.append(1)
num.append(2)
num.append(3)
num.append(4)
num.append(5)

print(num)

# output:
# [1, 2, 3, 4, 5]

# 10. Create a list of five animals. Add one animal using append() and insert another at a specific position using insert(). Display the final list.

# Creating a list of five animals
animals = ["cat", "dog", "tiger", "lion", "goat"]

# Adding rat at the end
animals.append("rat")

# Inserting rabbit at index 4
animals.insert(4, "rabbit")

# Displaying the final list
print(animals)

# output:
# ['cat', 'dog', 'tiger', 'lion', 'rabbit', 'goat', 'rat']

"""
Important methods to remember
Method	             |  What it does
---------------------------------------------------------------|
append(value)	     |  Adds one item at the end
insert(index, value) |	Adds an item at a specific position
extend(list)	     |  Adds all items from another iterable
"""



""" Removing Items from a List """

# 1. Create a list of five fruits and remove "banana" using remove().

# Creating a list of five fruits
fruit1 = ["apple", "banana", "orange", "cherry", "melon"]

# Removing banana
fruit1.remove("banana")

print(fruit1)

# output:
# ['apple', 'orange', 'cherry', 'melon']

# 2. Create a list of five numbers and remove the third item using pop().

# Creating a list of five numbers
numbers = [2, 55, 67, 8, 90]

# Removing the third item (index 2)
numbers.pop(2)

print(numbers)

# output:
# [2, 55, 8, 90]


# 3. Create a list of six colors and remove the last item using pop().

# Creating a list of six colors
color = ["red", "white", "gold", "orange", "blue", "silver"]

# Removing the last item
color.pop(5)

print(color)

# output:
# ['red', 'white', 'gold', 'orange', 'blue'] 

# 4. Create a list of five countries and delete the first item using del.

# Creating a list of five countries
countries = ["Nepal", "Japan", "Bhutan", "Australia", "United Kingdom"]

# Deleting the first item
del countries[0]

print(countries)

# output:
# ['Japan', 'Bhutan', 'Australia', 'United Kingdom']

# 5. Create a list of six student names and remove "John" using remove().

# Creating a list of six student names
students = ["Ram", "Shyan", "John", "Laxmi", "Sita", "Radha"]

# Removing John
students.remove("John")

print(students)

# output:
# ['Ram', 'Shyan', 'Laxmi', 'Sita', 'Radha']

# 6. Create a list containing duplicate numbers and remove one occurrence of a particular number.

# Creating a list containing duplicate numbers
numbers = [2, 55, 67, 8, 90, 67]

# Removing one occurrence of 67
numbers.remove(67)

print(numbers)

# output:
# [2, 55, 8, 90, 67]

# 7. Create a list of five programming languages and clear all its elements using clear().

# Creating a list of five programming languages
language = ["python", "c", "c++", "java", "js"]

# Removing all elements
language.clear()

print(language)

# output:
# []

# 8. Create a list of eight numbers and delete the elements from index 2 to index 5 using del.

# Creating a list of eight numbers
numbers = [2, 55, 67, 8, 90, 67, 11, 45]

# Deleting elements from index 2 up to index 5
del numbers[2:6]

print(numbers)

# output:
# [2, 55, 11, 45]

# 9. Create a list of five fruits and use pop() to remove the last element. Store the removed item in another variable and print it.

# fruit1 = ["apple", "banana", "orange", "cherry", "melon"]
# fruit1.pop(4)
# print(fruit1)

# fruit1 = ["apple", "banana", "orange", "cherry", "melon"]
# print(fruit1)

# 10. Create a list of five animals and remove one item using remove(), another using pop(), and another using del. Display the final list.

# animals = ["cat", "dog", "tiger", "lion", "goat"]
# animals.remove("dog")
# print(animals)

# animals.pop(4)
# print(animals)

# del animals[0]
# print(animals)