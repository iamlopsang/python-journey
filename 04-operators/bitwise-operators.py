    ## BITWISE OPERATOR IN PYTHON ##

"""Bitwise operators are used to perform operations on the binary representation of integers (0s and 1s).
Computers represent numbers in binary, a number system that uses only 0 and 1. 
Bitwise operators compare or shift these binary bits to produce a result.

Python has 6 main bitwise operators:
    - &,
    - |,
    - ^,
    - ~,
    - <<,
    - >>
    
Types of Bitwiase Operators:

| Operator | Name       | Example | Output| Explanation                                                       |
|---       |---         |---      |---    |---                                                                |
| `&`      | AND        | `5 & 3` | `1`   | Returns `1` if both corresponding bits are `1`.                   |
| `\|`     | OR         | `5 \| 3`| `7`   | Returns `1` if at least one corresponding bit is `1`.             |
| `^`      | XOR        | `5 ^ 3` | `6`   | Returns `1` if the corresponding bits are different.              |
| `~`      | NOT        | `~5`    | `-6`  | Inverts the bits of an integer.                                   |
| `<<`     | Left Shift | `5 << 1`| `10`  | Shifts the bits to the left by the specified number of positions. |
| `>>`     | Right Shift| `5 >> 1`| `2`   | Shifts the bits to the right by the specified number of positions.|

## Understanding Binary Numbers:
Before learning bitwise operators, understand how decimal numbers are represented in binary.

| Decimal Number | Binary Representation |
|---             |---                    |
| `1`            | `001`                 |
| `2`            | `010`                 |
| `3`            | `011`                 |
| `4`            | `100`                 |
| `5`            | `101`                 |
| `6`            | `110`                 |
| `7`            | `111`                 |

## Example:

- 5 in binary is 101.
- 3 in binary is 011.
Python can display an integer's binary representation using the bin() function.
"""
print(bin(5))  # Output: 0b101
print(bin(3))  # Output: 0b11

"""The prefix 0b indicates that the number is written in binary."""

## Bitwise AND (&):

"""The 'AND' operator returns '1' only when both corresponding bits are '1'. 
Otherwise, it returns '0'."""

## Example:
x = 5
y = 3

print(x & y)  # Output: 1

"""Explanation:
  5 = 101
  3 = 011
      ---
AND   001

Comapre each bit:

| Bit of 5 | Bit of 3 | Result |
|---       |---       |---     |
| `1`      | `0`      | `0`    |
| `0`      | `1`      | `0`    |
| `1`      | `1`      | `1`    |

The result is 001 in binary, which equals 1 in decimal."""

