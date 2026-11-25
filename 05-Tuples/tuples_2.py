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

"""10.3 Using break in  a tuple loop:

The break statement is used to stop a loop immediately when a specified condition is met.
"""

## Example:

# Creating a tuple of numbers
numbers = (10, 20, 30, 40, 50)

# Stopping the loop when the number is 30
for num in numbers:
    if num == 30:
        break
    print(num)

## output:

10
20

"""Explanation:
- The loop starts with 10 and prints it.
- Next, it accesses 20 and prints it.
- When it reaches 30, the condition num == 30 becomes True.
- The break statement immediately terminates the loop.
- Therefore, 30, 40, and 50 are not printed."""

"""10.4 Using continue in a tuple loop:

The continue statement skips the current iteration and moves to the next item in the loop.
"""

## Example:

# Creating a tuple of numbers
numbers = (10, 20, 30, 40, 50)

# Skipping the number 30
for num in numbers:
    if num == 30:
        continue
    print(num)

## output:

10
20
40
50

"""Explanation:
- The loop accesses each number one by one.
- When it reaches 30, the condition becomes True.
- The continue statement skips the current iteration.
- Therefore, 30 is not printed.
- The loop continues with 40 and 50."""

"""note:
Statement	|   Purpose                                             |
---------------------------------------------------------------------
break	    |   Terminates the entire loop.                         |
continue	|   Skips the current iteration and continues the loop. |"""

"""11. Looping Through Tuples Using a while Loop:

    What is a while Loop?

    A while loop is used to execute a block of code repeatedly as long as a specified condition is True.
    When looping through a tuple, a while loop uses index numbers to access each item one by one.
    Unlike a for loop, a while loop requires you to manually manage the index number.
    """

## 11.1 Using a while Loop to Access Tuple Items
    
    # Syntax:

""" while condition:
        # Code to execute
        # Update the index """

## Example:

# Creating a tuple of fruits
fruits = ("apple", "banana", "cherry", "orange")

# Initializing the index
i = 0

# Looping through the tuple
while i < len(fruits):
    print(fruits[i])
    i += 1

## output:

# apple
# banana
# cherry
# orange

"""Explanation:

Let's understand the code step by step.
1. i = 0 initializes the index at 0, which represents the first item.
2. while i < len(fruits) checks whether the index is smaller than the total number of items.
3. print(fruits[i]) accesses and displays the item at the current index.
4. i += 1 increases the index by 1 after each iteration.
5. The loop continues until i becomes 4.
6. When i becomes 4, the condition 4 < 4 becomes False, and the loop stops."""


""" 11.2 Looping Through a Tuple Using Negative Indexing:

You can also use negative indexing with a while loop to access tuple items from the end to the beginning."""

## Example:

# Creating a tuple of fruits
fruits = ("apple", "banana", "cherry", "orange")

# Initializing the negative index
i = -1

# Looping through the tuple in reverse order
while i >= -len(fruits):
    print(fruits[i])
    i -= 1

## output:

# orange
# cherry
# banana
# apple

"""Explanation:
- i = -1 starts from the last item.
- -len(fruits) returns -4, which represents the first item.
- fruits[i] accesses the item at the current negative index.
- i -= 1 decreases the index by 1 after each iteration.
- The loop stops when i becomes -5 because the condition is no longer True."""

"""11.3 Using a while Loop with a Conditional Statement:

You can combine a while loop with an if statement to check conditions for each tuple item."""

## Example:

# Creating a tuple of numbers
numbers = (10, 15, 20, 25, 30, 35)

# Initializing the index
i = 0

# Looping through the tuple
while i < len(numbers):

    # Checking for even numbers
    if numbers[i] % 2 == 0:
        print(numbers[i])

    # Increasing the index
    i += 1

## output:

10
20
30

"""Explanation:
- The while loop accesses each number using its index.
- numbers[i] % 2 == 0 checks whether the current number is even.
- If the condition is True, the number is printed.
- If the condition is False, Python skips the print() statement.
- i += 1 moves to the next index."""

