##        Python Chapter 04 — Operators

    
    ## About This Chapter:

    This chapter covers the different types of operators in Python. It explores how operators are used to perform mathematical calculations, assign values, compare data, evaluate conditions, check object identity and membership, and perform operations on binary numbers.

    ## Types of Operators:
    
    There are seven types of operators and they are as follows:

        > Arithmetic operators
        > Assignment operators
        > Comparison operators
        > Logical operators
        > Identity operators
        > Membership operators
        > Bitwise operators

    ## Topics Covered:

    1. Arithmetic Operators (arithmetic.py)

    Arithmetic operators are used to perform mathematical calculations.

    | Operator | Name           | Description                             | Example       |
    |---       |---             |---                                      |---            |
    | `+`      | Addition       | Adds two values                         | `10 + 5 = 15` |
    | `-`      | Subtraction    | Subtracts one value from another        | `10 - 5 = 5`  |
    | `*`      | Multiplication | Multiplies two values                   | `10 * 5 = 50` |
    | `/`      | Division       | Divides two values and returns a float  | `10 / 5 = 2.0'|
    | `%`      | Modulus        | Returns the remainder                   | `10 % 3 = 1`  |
    | `//`     | Floor Division | Returns the division result rounded down| `10 // 3 = 3` |
    | `**`     | Exponentiation | Raises a number to the power of another | `2 ** 3 = 8`  |

    Example:

    a = 10
    b = 3

    print(a + b)  # Output: 13
    print(a % b)  # Output: 1
    print(a // b) # Output: 3

    2. Assignment Operators (assignment.py)

    Assignment operators are used to assign values to variables and update their existing values.

    | Operator | Name                     | Description                                   | Example        |
    |---       |---                       |---                                            |---             |
    | `=`      | Assignment               | Assigns a value to a variable                 | `x = 5`        |
    | `+=`     | Addition Assignment      | Adds a value and assigns the result           | `x += 3`       |
    | `-=`     | Subtraction Assignment   | Subtracts a value and assigns the result      | `x -= 3`       |
    | `*=`     | Multiplication Assignment| Multiplies and assigns the result             | `x *= 3`       |
    | `/=`     | Division Assignment      | Divides and assigns the result                | `x /= 3`       |
    | `%=`     | Modulus Assignment       | Assigns the remainder                         | `x %= 3`       |
    | `//=`    | Floor Division Assignment| Performs floor division and assigns the result| `x //= 3`      |
    | `**=`    | Exponentiation Assignment| Raises to a power and assigns the result      | `x **= 3`      |
    | `&=`     | AND Assignment           | Performs bitwise AND and assigns the result   | `x &= 3`       |
    | `\|=`    | OR Assignment            | Performs bitwise OR and assigns the result    | `x \|= 3`      |
    | `^=`     | XOR Assignment           | Performs bitwise XOR and assigns the result   | `x ^= 3`       |
    | `>>=`    | Right Shift Assignment   | Shifts bits right and assigns the result      | `x >>= 3`      |
    | `<<=`    | Left Shift Assignment    | Shifts bits left and assigns the result       | `x <<= 3`      |
    | `:=`     | Walrus Operator          | Assigns a value inside an expression          | `print(x := 5)`|

    Example:

    number = 10
    number += 5

    print(number)  # Output: 15

    3. Comparison Operators (comparison.py)

    Comparison operators are used to compare two values. They return either True or False.

    | Operator | Name                  | Description                                       | Example            |
    |---       |---                    |---                                                |---                 |
    | `==`     | Equal                 | Checks if two values are equal                    | `10 == 10` → `True`|
    | `!=`     | Not Equal             | Checks if two values are different                | `10 != 5` → `True` |
    | `>`      | Greater Than          | Checks if the left value is greater               | `10 > 5` → `True`  |
    | `<`      | Less Than             | Checks if the left value is smaller               | `5 < 10` → `True`  |
    | `>=`     | Greater Than or Equal | Checks if the left value is greater than or equal | `10 >= 10` → `True`|
    | `<=`     | Less Than or Equal    | Checks if the left value is smaller than or equal | `5 <= 10` → `True` |

    Example:

    a = 10
    b = 5

    print(a > b)  # Output: True
    print(a == b) # Output: False


    4. Logical Operators (logical.py)

    Logical operators are used to combine multiple conditions or reverse the result of a condition.

    | Operator | Name       | Description                                      | Example                      |
    |---       |---         |---                                               |---                           |
    | `and`    | Logical AND| Returns `True` if both conditions are true       | `10 > 5 and 10 < 20` → `True`|
    | `or`     | Logical OR | Returns `True` if at least one condition is true | `10 < 5 or 10 > 5` → `True`  |
    | `not`    | Logical NOT| Reverses the result of a condition               | `not(10 > 5)` → `False`      |

    Example:

    age = 20

    print(age >= 18 and age <= 60)  # Output: True
    print(not age >= 18)            # Output: False

5. Identity Operators (identity.py)

Identity operators are used to check whether two variables refer to the same object in memory. They are different from comparison operators, which compare values.


| Operator | Name | Description | Example |
|---|---|---|---|
| `is` | Identity | Returns `True` if both variables refer to the same object | `a is b` |
| `is not` | Not Identity | Returns `True` if both variables refer to different objects | `a is not b` |

Example:

a = [1, 2, 3]
b = a

print(a is b)  # Output: True


6. Membership Operators (membership.py)

Membership operators are used to check whether a value exists in a sequence or collection, such as a string, list, tuple, set, or dictionary.

| Operator | Name | Description | Example |
|---|---|---|---|
| `in` | Membership | Returns `True` if a value exists in a sequence | `"apple" in ["apple", "banana"]` → `True` |
| `not in` | Not Membership | Returns `True` if a value does not exist in a sequence | `"mango" not in ["apple", "banana"]` → `True` |


Example:

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)      # Output: True
print("orange" not in fruits) # Output: True


7. Bitwise Operators (bitwise.py)

Bitwise operators are used to perform operations on the binary representation of integers (0s and 1s).


| Operator | Name | Description | Example |
|---|---|---|---|
| `&` | AND | Sets each bit to 1 if both bits are 1 | `5 & 3 = 1` |
| `\|` | OR | Sets each bit to 1 if at least one bit is 1 | `5 \| 3 = 7` |
| `^` | XOR | Sets each bit to 1 if the bits are different | `5 ^ 3 = 6` |
| `~` | NOT | Inverts all bits | `~5 = -6` |
| `<<` | Left Shift | Shifts bits to the left | `5 << 1 = 10` |
| `>>` | Right Shift | Shifts bits to the right | `5 >> 1 = 2` |

Example:

a = 5
b = 3

print(a & b)  # Output: 1

