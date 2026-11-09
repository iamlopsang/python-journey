"""Python Lists Exercises
This file contains a series of exercises to help you practice working with Python lists."""

""" Creating Lists """ 
# 1. Create a list containing five different fruits and print the list.

# Creating a list of five different fruits
fruits = ["apple", "banana", "orange", "cherry", "melon"]

# Printing the complete list
print(fruits)
# 2. Create a list containing five integer numbers.

# Creating a list of five integers
numbers = [1, 2, 3, 4, 6]

# Printing the list
print(numbers)
# 3. Create a list containing your name, age, GPA, and student status.

# Creating a list with different data types
student = ["Leon", 26, 3.89, "Active"]

# Printing student information
print(student)

# 4. Create an empty list and print it.

# Creating an empty list
fruits = []

# Printing the empty list
print(fruits)

# 5. Create a list containing both integers and strings.

# Creating a list containing integers and strings
friends = [6, 7, "hello", 9, "hi"]

# Printing the list
print(friends)

# 6. Create a list containing five different student names. Print each item using print().

# Creating a list of five student names
students = ["Ram", "Shyan", "Laxmi", "Sita", "Radha"]

# Printing each item using its index
print(students[0])  # Prints Ram
print(students[1])  # Prints Shyan
print(students[2])  # Prints Laxmi
print(students[3])  # Prints Sita
print(students[4])  # Prints Radha

# 7. Create a list containing duplicate values and display it.

# Creating a list containing duplicate values

color = ["red", "white", "gold", "red", "blue"]

# Printing the list
print(color)

# 8. Create a list containing three different data types: string, integer, and float.

# Creating a list with string, integer, and float values

customer = ["Kathmandu", 3345, 456.89]

# Printing the list
print(customer)

# 9. Create two separate lists: one containing five even numbers and another containing five odd numbers.

# Creating a list of five even numbers
even = [2, 4, 6, 8, 10]

# Creating a list of five odd numbers
odd = [1, 3, 5, 7, 9]

# Printing both lists
print(even)
print(odd)

# 10. Create a list containing the names of five programming languages and print the total list.

# Creating a list of five programming languages
language = ["python", "c", "c++", "java", "js"]

# Printing the complete list
print(language)

# Counting the total number of items
total_list = len(language)

# Printing the total count
print(total_list)

""" 2. Accessing List Items"""

# 1. Create a list of five fruits and print the first item.

# Creating a list of five fruits
fruits = ["apple", "banana", "orange", "cherry", "melon"]

# Accessing the first item using index 0
print(fruits[0])

# 2. Create a list of five countries and print the third item.

# Creating a list of five countries
countries = ["Nepal", "Bhutan", "China", "Maldives", "UK"]

# Accessing the third item using index 2
print(countries[2])

# 3. Create a list of six numbers and print the last item using positive indexing.

# Creating a list of six numbers
numbers = [2, 55, 67, 8, 90, 55]

# Accessing the last item using positive indexing
print(numbers[5])

# 4. Create a list of five colors and print the second-last item using negative indexing.

# Creating a list of five colors
color = ["red", "white", "gold", "orange", "blue"]

# Accessing the second-last item using negative indexing
print(color[-2])

# 5. Create a list of seven numbers and print the first, fourth, and last items.

# numbers= [2,55,67,8,90,55, 11]
# print(numbers[0])
# print(numbers[3])
# print(numbers[6])

# 6. Create a list of five student names and access the name at index 2.

# students = ["Ram", "Shyan", "Laxmi", "Sita", "Radha"]
# print(students[2])


# 7. Create a list of six programming languages and print the first and last languages.

# language = ["python", "c", "c++", "java", "js", "c#"]
# print(language[0])
# print(language[5])

# 8. Create a list of five animals and access the items using negative indexes -1, -3, and -5.

# animals=["cat","dog", "tiger", "lion","goat"]
# print(animals[-1])
# print(animals[-3])
# print(animals[-5])