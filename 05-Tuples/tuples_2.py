"""10. Looping Through Tuples Using a for Loop:

What is Looping Through a Tuple?

    Looping through a tuple means accessing each item in a tuple one by one using a loop.
    A for loop is commonly used to iterate through a tuple and execute a block of code for every item.
    Since tuples are ordered, Python accesses their items in the same order they were stored.

    ## Using a for Loop to Access Tuple Items:

    Syntax:

        for variable in tuple_name:
        
        for starts the loop.

    Explanation:

    variable temporarily stores the current item.
    in tells Python which tuple to iterate through.
    The indented code executes for every item.
"""

## Example:

# Creating a tuple of fruits
fruits = ("apple", "banana", "cherry", "orange")

# Accessing each item using a for loop
for fruit in fruits:
    print(fruit)

## output:

# apple
# banana
# cherry
# orange

"""Explanation:
1. Python starts with the first item "apple".
2. It stores that item in the variable fruit.
3. The print() statement displays the current item.
4. The loop moves to the next item.
5. This process continues until all tuple items have been accessed."""

"""10.1 Looping through a tuple using index numbers:

You can also use a for loop with the range() and len() functions to access tuple items through their index numbers."""

##  Example:

# Creating a tuple of fruits
fruits = ("apple", "banana", "cherry", "orange")

# Looping through tuple using index numbers
for i in range(len(fruits)):
    print(fruits[i])

## output:

# apple
# banana
# cherry
# orange

"""Explanation:
- len(fruits) returns 4 because the tuple contains four items.
- range(4) generates index numbers 0, 1, 2, 3.
- The variable i stores each index number.
- fruits[i] accesses the item at the current index.
- The loop continues until all four items are displayed."""

"""10.2 Looping through a tuple with a conditional statement:

You can combine a for loop with an if statement to check conditions for each item in a tuple.
"""

## Example:

# Creating a tuple of numbers
numbers = (10, 15, 20, 25, 30, 35)

# Displaying only even numbers
for num in numbers:
    if num % 2 == 0:
        print(num)

## output:

10
20
30

"""Explanation:
- The for loop accesses each number one by one.
- num % 2 == 0 checks whether the current number is divisible by 2.
- If the condition is True, Python prints the number.
- If the condition is False, Python skips the print() statement and moves to the next item."""