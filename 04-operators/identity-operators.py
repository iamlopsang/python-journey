    ## IDENTITY OPERATORS IN PYTHON ##

"""Identity operators are used to check whether two variables refer to the same object in memory.
They return either 'True' or 'False'.
Python has two identity operators:
    > is 
    > is not
    
    Types of Identity Operators
    
    | Operator | Name             | Example      | Output            | Explanation                                                |
    |---       |---               | ---          |---                |---                                                         |
    | `is`     | Identity         | `x is y`     | `True` or `False` | Returns `True` if both variables refer to the same object. |
    | `is not` | Negative Identity| `x is not y` | `True` or `False` | Returns `True` if the variables refer to different objects.|"""

## is operator:
"""The 'is' operator checks whether two variable refer to the same object, not just whether they have the same value.
"""

## Example:

x = [1, 2, 3]
y = x

print(x is y)  # Output: True

"""
Explanation:
- x refers to a list containing [1, 2, 3].
- y = x makes y refer to the same list as x.
- Therefore, x is y returns True.
"""

## is not operator:

"""The 'is not' operator checks whether two variables refer to different objects.
"""

## Example:

x = [1, 2, 3]
y = [1, 2, 3]

print(x is not y)  # Output: True

"""Difference Between == and is
This is the most important concept to understand about identity operators.

| Operator | Purpose                                                | Example  | Output |
|---       |---                                                     |---       |---     |
| `==`     | Checks whether two objects have equal values.          | `x == y` | `True` |
| `is`     | Checks whether two variables refer to the same object. | `x is y` | `False`|
"""
## Example:

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # Output: True
print(x is y)  # Output: False

"""Explanation:
- x == y returns True because both lists contain the same values.
- x is y returns False because the lists are two separate objects.
Think of it this way: == compares values, while is compares object identity."""

## Practical Example: Using 'is' with 'none':
"""Identity operators are commonly used to check whether a variable is 'None'."""

name = None

if name is None:
    print("Name is not provided.")
else:
    print(name)

## Output:
"""Name is not provided.

Explanation: name is None checks whether name refers to Python's special None object. Since it does, the condition is True."""
