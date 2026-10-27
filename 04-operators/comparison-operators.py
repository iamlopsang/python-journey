    ## COMPARISON OPERATORS IN PYTHON ##

"""Comparison operators are used to compare two values. 
They check whether a condition is true or false and return a Boolean value: True or False.

They are commonly used in 'if-else' statements and loops to make decision in Python.

## Types of Comparison operators in Python:

| Operator | Name                     | Example | Output | Explanation                                                                |
|---       |---                       |---      |---     |---                                                                         |  
| `==`     | Equal to                 | `5 == 5`| `True` | Checks whether two values are equal.                                       |
| `!=`     | Not equal to             | `5 != 3`| `True` | Checks whether two values are not equal.                                   |
| `>`      | Greater than             | `8 > 5` | `True` | Checks whether the left value is greater than the right value.             |
| `<`      | Less than                | `3 < 5` | `True` | Checks whether the left value is less than the right value.                |
| `>=`     | Greater than or equal to | `5 >= 5`| `True` | Checks whether the left value is greater than or equal to the right value. |
| `<=`     | Less than or equal to    | `3 <= 5`| `True` | Checks whether the left value is less than or equal to the right value.    |

"""
"""Python compares the values on both sides of an operator and returns either 'True' or 'False', depending on the result."""

## Equal to:

x = 10
y = 10

print(x == y)  # Output: True

"""Explanation: Both variables contain the same value, so the result is True."""

## Not equal to:

x = 10
y = 5

print(x != y)  # Output: True

"""Explanation: The values are different, so the result is True."""

## Greater than:

x = 10
y = 5

print(x > y)  # Output: True

"""Explanation: 10 is greater than 5, so the result is True."""

## Less than:

x = 3
y = 8

print(x < y)  # Output: True

"""Explanation: 3 is less than 8, so the result is True."""

## Greater than or equal to:

x = 10
y = 10

print(x >= y)  # Output: True

"""Explanation: Both values are equal. The condition is True because >= allows the values to be equal."""

## Less than or equal to:

x = 4
y = 7

print(x <= y)  # Output: True

"""Explanation: 4 is less than 7, so the result is True."""


