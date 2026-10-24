        ## PYTHON BOOLEAN ##

"""A Boolean represents one of two values:
    > True
    > False"""

# Example:

is_student = True
is_logged = False

##  Boolean Values from Comparisons:

x = 10
y = 5
print(x>y)  # Output -> True

print(x<y)  # Output -> False

## Boolean Values From Condition:
"""Conditions can also produce Boolean results."""

# Example:

age = 20
if age >= 18:
    print("Adult")

# Output -> Adult     

## bool() Function:
"""The bool() function converts a value into a Boolean"""

# Example:

print(bool(1))  # Output -> True

print(bool(0))  # Output -> False

"""Note: Generally, values such as "0", None, and empty collections are considered as "False" in Boolean
 contexts, while many other values are considered as "True" """

# Example:

print(bool("Hello"))    # Output -> True
print(bool(" "))        # Output -> False
print(bool("10"))       # Output -> True
print(bool("0"))        # Output -> False







