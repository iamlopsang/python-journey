    ## MEMBERSHIP OPERATOR IN PYTHON ##

"""Membership operators are used to check whether a value exists in a sequence or collection, such as a string,
list, tuple, set, or dictionary.

Python has two membership operators:
    > in
    > not in
    
They return 'True' or 'Flase' depending on whether the value is found.

Types of Membership Operators:

| Operator | Name                | Example             | Output | Explanation                                                              |
|---       |---                  |---                  |---     |---                                                                       |
| `in`     | Membership          | `"a" in "apple"`    | `True` | Returns `True` if the value exists in the sequence or collection.        |
| `not in` | Negative Membership | `"z" not in "apple"`| `True` | Returns `True` if the value does not exist in the sequence or collection.|
"""

## in operator:

"""The 'in' operator checks whether a value exists in a sequence or collection."""

## Example 1: With a String:-

text = "Python"

print("P" in text)  # Output: True
print("z" in text)  # Output: False

"""Explanation:
- "P" in text returns True because "P" exists in "Python".
- "z" in text returns False because "z" does not exist in "Python"."""

## Example 2: With List

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)  # Output: True
print("grapes" in fruits)  # Output: False

"""Explanation:
- "apple" in fruits returns True because "apple" is in the list.
- "grapes" in fruits returns False because "grapes" is not in the list."""

## not in operator:

"""The 'not in' operator checks whether a value is absent from a sequence or collection."""

## Example : With a List

fruits = ["apple", "banana", "mango"]

print("grapes" not in fruits)  # Output: True
print("apple" not in fruits)   # Output: False

"""Explanation:
- "grapes" not in fruits returns True because "grapes" is not in the list.
- "apple" not in fruits returns False because "apple" exists in the list."""

"""Note: When using membership operators with a dictionary, Python check its keys, not its values."""

## Example:

student = {"name": "John", "age": 20}

print("name" in student)  # Output: True
print("John" in student) # Output: False

"""'name' is a dictionary key, but 'John' is a value."""


