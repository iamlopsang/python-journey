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