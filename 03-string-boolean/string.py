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

