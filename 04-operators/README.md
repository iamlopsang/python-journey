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
