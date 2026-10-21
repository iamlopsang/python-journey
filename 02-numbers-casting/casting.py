        ## Casting in Python ##

## Python provides built-in functions to convert between different numeric types.
# For example, you can convert an integer to a float or a complex number, and vice versa.
# there are four main functions for casting in Python:
# 1. int() - converts a value to an integer
# 2. float() - converts a value to a float
# 3. complex() - converts a value to a complex number
# 4. str() - converts a value to a string

## int() function:

x = int(1)
y = int(2.8)  # converts float to int (truncates decimal part)
z = int("3")  # converts string to int

## float() function:

x = float(1)  # converts int to float
y = float(2.8)  # converts float to float (no change)
z = float("3.14")  # converts string to float

## complex() function:

x = complex(1)  # converts int to complex
y = complex(2.8)  # converts float to complex
z = complex("3+4j")  # converts string to complex

### str() function:

x = str(1)  # converts int to string
y = str(2.8)  # converts float to string
z = str(3 + 4j)  # converts complex to string



