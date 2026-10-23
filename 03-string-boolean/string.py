            ##  PYTHON STRING   ##

## To create a string in Python:

name = "John"

## Strings with multiple lines:

message = """Welcome to the world of Python programming."""

## Strings are arrays:

name = "Harry"
print(name[0])  # Output: H

## Looping through a string:

city = "New York"

for letter in city:
    print(letter)

## String length:

letters = "programming"

print(len(letters))  # Output: 11

## Checking if a word or phrase is present in a string:

text = "Python is a programming language."
print("Python" in text)  # Output: True

## String slicing:

## Slicing allows you to extract a portion of a string by specifying the start and end indices.
# and there are many more string methods available in Python that can be used to manipulate and work
# with strings effectively.

text = "Hello, World!"
print(text[0:5])  # Output: Hello

## Slice from the start:

city="Kathmandu"
print(city[:3])  # Output: Kat

## Slice to the end:

city = "Kathmandu"
print(city[4:])  # Output: mandu

## Negative indexing:

city = "Kathmandu"
print(city[-3:])  # Output: ndu

## Negative slicing:

city = "Kathmandu"
print(city[-6:-3])  # Output: tha

## Modifying strings:

message = "Wello, World!"
new_message = "H" + message[1:]
print(new_message)  # Output: Hello, World!

## Common String Methods:
# Python provides many built-in  string methods:

## upper():
text = "Hello"
print(text.upper()) #HELLO

## lower():
text = "Hello"
print(text.lower()) #hello

## strip():
text = " Hello "
print(text.strip()) #Hello - removes unwanted or unneccessary white space

## replace():
text = "Hello"
print(text.replace("Hello","Welcome"))

## split():

fruits = "apple, banana, cherry"
print(fruits.split(",")) 
# ['apple', 'banana', 'cherry'] --splits a string into parts

## String Concatenation:

first_name = "Jack"
last_name = "Sparrow"

fullname = first_name + " " +last_name

print(fullname) # Jack Sparrow

## String Formatting:
# f - strings are a convenient method

name = "Elsa"
age = 21

print(f"Her name is {name}. and Her age is {age}.")

## Escape Characters:
# An escape character allows you to include special characters inside a string.

## New line (\n):
print("Hello \n World")

    ## Output:
        # Hello
        # World

## Tab (\t):
print("Hello \t World")

    ## Output:
        # Hello World

## Double and Single quote:
# Useful when the string itself uses double or single quotes.

message = "She said \"Hello\" "  # She said "Hello"

text = 'It\'s Python'  # It's Python

