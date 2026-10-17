# Variables and Data Types — Exercises

## Variables

# 1. Create variables for your name, age, and country. Print their values.

name = "Mark"
age = 27
country = "Canada"

print("Name:", name)
print("Age:", age)
print("Country:", country)

# 2. Assign three different values to three variables in a single line.

x,y,z = 23, 27, 31

# 3. Assign the same value to three variables.

i = j = k = 95

# 4. Create a variable named `total_marks` and print it.

total_marks = 98

print("Total_marks:", total_marks)

# 5. Write a program to print Hello, World!.

print("Hello, World!")

# 6. Write a program to print your full name.

name = "Mark Johnson"
print("Full Name:", name)

# 7. Write a program to print your name, age, and address on separate lines.

name = "Alessica"
age = 30
address = "123 Main St, Toronto, Canada"

print("Name:", name)
print("Age:", age)
print("Address:", address)

# 8. Write a program to accept the user's name and print a welcome message.

user_name = input("Enter your name:")

print("Welcome,", user_name)

# 9. Write a program to accept the user's name and age, then display both.

user_name = input("Enter your name:")
user_age = input("Enter your age:")

print("Name:", user_name)
print("Age:", user_age)

# 10. Write a program to accept the user's name and print:

# Hello, Prakash!
# Welcome to Python programming.

user_name = input("Enter your name:")

print("Hello,", user_name + "!")
print("Welcome to Python programming.")

# 11. Write a program to accept two numbers and display them.

num1 = input("Enter a first number:")
num2 = input("Enter a second number:")

print("the first number is :", num1)
print("the second number is :", num2)

# 12. Write a program to accept your first name and last name separately and print your full name.

first_name = input("Enter your first name:")
last_name = input("Enter your last name:")

print("Full Name of the user is :", first_name + " " + last_name)

# 13. Write a program to accept a favorite color and print a message using that color.
color = input("Enter your favourite color:")
print("Your favourite color is :", color)

# 14. Write a program to accept the user's name, age,
#  and favorite programming language and display them in a formatted message.

name = input("Enter your name :")
age = input("Enter your age :")
programming_language = input("Enter your favourite programming language :")

print("Hello, my name is", name + ". I am", age, "years old and my favourite programming language is", programming_language + ".")

## Data Types

# 5. Create one variable each of type `str`, `int`, `float`, and `bool`.

name = 'John'
age = 25
price = 30.45
is_rainy = True

# 6. Use `type()` to check the data type of each variable.

name = 'Alina'
age = 35
total_price = 76.70
is_sunny = False

print(type(name))
print(type(age))
print(type(total_price))    
print(type(is_sunny))

# 7. Create a list, tuple, set, and dictionary.

fruits = ['apple', 'banana', 'cherry']

colors = ('red', 'green', 'blue')

animals = {'cat', 'dog', 'rabbit'}

section_a = {
    "name":"Elsa",
    "age": 24,
    "gpa" : 3.8
}
# 8. Create a variable with the value `None` and check its type.

shoes = None

print(type(shoes))

# ## Challenge

# 9. Create variables representing a student's name, age, marks, and enrollment status. Print each 
# value and its data type.

student_name = "Naruto Uzumaki"
student_age = 17
student_marks = 85.5
student_enrollment_status = True

print ("Student Name :", student_name, type(student_name))
print("Age of Student:", student_age, type(student_age))
print("Student Marks:", student_marks, type(student_marks))
print("Enrollment Status:", student_enrollment_status, type(student_enrollment_status))

# 10. Create variables to store your name, age, height, and whether you are a student. Print all four
#  variables.

name = "Sasuke Uchiha"
age = 17
height = 175.5
is_student = True

print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Is Student:", is_student, type(is_student))  

# 11. Create two integer variables and print their values.

num1 = 10
num2 = 20

print("First Number:", num1)
print("Second Number:", num2)

# 12. Create a variable containing a decimal number and print it.

num3 = 30.5

print("Decimal Number:", num3)

# 13. Store your name in a variable and print its data type using type().

name = "Sakura Haruno"

print("Name of the user:", name, type(name))

# 14. Accept a number from the user and print its type before and after converting it to an integer.

num = input("Enter a number (float number or decimal number):")
print("Before the conversion, the type of the number is:", type(num))

num = int(num)
print("After the conversion, the type of the number is:", type(num))

# 15. Accept two numbers as input and print their sum after converting them to integers.

num1 = input("Enter the first number:")
num2= input("Enter the second number:")

sum= int(num1)+int(num2)

print("The sum of the two numbers is:", sum, type(sum))

# 16. Accept a decimal number from the user and convert it to a float.

num = input("Enter a decimal number:")

num = float(num)

print("The decimal number is:", num, type(num))

# 17. Accept a number as a string and convert it to an integer. Print the result.

name = input("Enter a number as a string:")
name = int(name)

print("The number is:", name, type(name))

# 18. Accept a user's age and print the age after converting it to an integer.

age = input("Enter your age:")
age = int(age)

print("Your age is:", age, type(age))



