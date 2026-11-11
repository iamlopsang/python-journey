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

# students = ["Ram", "Shyan", "Laxmi", "Sita", "Radha"]

# print("Gita" in students)

# 6. Create a list of programming languages and check whether "Python" is present using in.

# language = ["python", "c", "c++", "java", "js", "c#"]
# print("python" in language)

# 7. Create a list of five animals and check whether "lion" is absent using not in.

# animals = ["cat", "dog", "tiger", "lion", "goat"]
#  print("lion" not in animals)