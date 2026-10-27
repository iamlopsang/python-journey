        ## LOGICAL OPERATORS IN PYTHON ##

"""Logical operators  are used to combine multiple conditions or reverse a condition.
They return 'True' or 'False' based on the conditons being checked.

Python has three logical operators:
    > and,
    > or,
    > not
    
    TYPES OF LOGICAL OPERATORS:

    | Operator | Name       | Example           | Output | Explanation                                                              |
    |---       |---         |---                |---     |---                                                                       |
    | `and`    | Logical AND| `5 > 2 and 10 > 5`| `True` | Returns `True` if both conditions are `True`.                            |
    | `or`     | Logical OR | `5 > 2 or 10 < 5` | `True` | Returns `True` if at least one condition is `True`.                      |
    | `not`    | Logical NOT| `not(5 > 2)`      | `False`| Reverses the result: `True` becomes `False`, and `False` becomes `True`. |"""

## AND (and) operator:

"""The and operator returns True only when both conditions are True.
 If either condition is False, the result is False."""

# Example:

x = 10

print(x > 5 and x < 20)  # Output: True
print(x > 5 and x < 8)   # Output: False
print(x < 5 and x < 20)  # Output: False

"""Truth Table

| Condition 1 | Condition 2 | Result  |
|---          |---          |---      |
| `True`      | `True`      | `True`  |
| `True`      | `False`     | `False` |
| `False`     | `True`      | `False` |
| `False`     | `False`     | `False` |"""

## OR (or) operator:

"""The or operator returns True if at least one condition is True. 
It returns False only when both conditions are False."""

# Example:

x = 10

print(x > 5 or x < 8)   # Output: True
print(x < 5 or x < 20)  # Output: True
print(x < 5 or x > 20)  # Output: False

"""
Truth Table:

| Condition 1 | Condition 2 | Result |
|---          |---          |---     |
| `True`      | `True`      | `True` |
| `True`      | `False`     | `True` |
| `False`     | `True`      | `True` |
| `False`     | `False`     | `False`|"""






