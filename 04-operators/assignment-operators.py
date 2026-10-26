        ## ASSIGNMENT OPERATORS IN PYTHON ##

"""Assignment operators assign values to variables.

| Operator | Example        | Same As                                  | Explanation                                                                                                              |
|---       |---             |---                                       |                                                                                                                       ---|
| `=`      | `x = 10`       | `x = 10`                                 | Assigns the value `10` to `x`.                                                                                           |
| `+=`     | `x += 5`       | `x = x + 5`                              | Adds `5` to `x` and assigns the result to `x`.                                                                           |
| `-=`     | `x -= 3`       | `x = x - 3`                              | Subtracts `3` from `x` and assigns the result to `x`.                                                                    |
| `*=`     | `x *= 2`       | `x = x * 2`                              | Multiplies `x` by `2` and assigns the result to `x`.                                                                     |
| `/=`     | `x /= 2`       | `x = x / 2`                              | Divides `x` by `2` and assigns the result to `x`.                                                                        |
| `%=`     | `x %= 3`       | `x = x % 3`                              | Assigns the remainder of `x` divided by `3` to `x`.                                                                      |
| `//=`    | `x //= 3`      | `x = x // 3`                             | Performs floor division and assigns the result to `x`.                                                                   |
| `**=`    | `x **= 2`      | `x = x ** 2`                             | Raises `x` to the power of `2` and assigns the result to `x`.                                                            |
| `&=`     | `x &= 3`       | `x = x & 3`                              | Performs a bitwise AND operation and assigns the result to `x`.                                                          |
| `\|=`    | `x \|= 3`      | `x = x \| 3`                             | Performs a bitwise OR operation and assigns the result to `x`.                                                           |
| `^=`     | `x ^= 3`       | `x = x ^ 3`                              | Performs a bitwise XOR operation and assigns the result to `x`.                                                          |
| `>>=`    | `x >>= 1`      | `x = x >> 1`                             | Shifts the bits of `x` to the right by one position.                                                                     |
| `<<=`    | `x <<= 1`      | `x = x << 1`                             | Shifts the bits of `x` to the left by one position.                                                                      |
| `:=`     |`print(x := 5)` | Assigns `5` to `x` within an expression. | Assigns a value to a variable as part of an expression. This is called the *assignment expression* or *walrus operator*. |


"""

## Basic Assignment operator:

x = 10
print(x)  # Output: 10

## Addition Assignment operator:

x = 10
x += 5
print(x)  # Output: 15

## Subtraction Assignment operator:

x = 10
x -= 3
print(x)  # Output: 7

## Multiplication Assignment operator:

x = 10
x *= 2
print(x)  # Output: 20

## Division Assignment operator:

x = 10
x /= 2
print(x)  # Output: 5.0

## Modulus Assignment operator:

x = 10
x %= 3
print(x)  # Output: 1

## Floor Division Assignment operator:

x = 10
x //= 3
print(x)  # Output: 3

## Exponential Assignment operator:

x = 2
x **= 3
print(x)  # Output: 8

## Bitwise AND Assignment :

x = 5
x &= 3
print(x)  # Output: 1

"""Performs a bitwise AND operation on the binary values of 5 (101) and 3 (011)."""

