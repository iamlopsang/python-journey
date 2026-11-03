        ## Practice question based on Operator in Python ##
 
"""
Arithmetic Operators
Operators: +, -, *, /, %, //, **"""


# 1. Write a program that takes two numbers as input and displays their sum, difference, product, and quotient.

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

total = num1 + num2  # Explanation: Adds the two numbers.
difference = num1 - num2  # Explanation: Subtracts the second number from the first.
product = num1 * num2  # Explanation: Multiplies the two numbers.
quotient = num1 / num2  # Explanation: Divides the first number by the second.

print(total)    
print(difference)
print(product)
print(quotient)

# 2. Write a program that takes the length and width of a rectangle as input and calculates its area and perimeter.

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width  # Explanation: Multiplies length by width to calculate the area.
perimeter = 2 * (length + width)  # Explanation: Adds length and width, then multiplies by 2.

print(area)
print(perimeter)

# 3. Write a program that takes the price of an item and its quantity as input and calculates the total cost.

quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price of one item: "))

total_cost = quantity * price  # Explanation: Multiplies the quantity by the price of one item.

print(total_cost)

# 4. Write a program that takes a number of minutes as input and converts it into hours and remaining minutes. Use floor division and modulus.

minutes = int(input("Enter the number of minutes: "))

hours = minutes // 60  # Explanation: Uses floor division to calculate complete hours.
remaining_minutes = minutes % 60  # Explanation: Gets the minutes remaining after dividing by 60.

print("Hours:", hours)
print("Remaining minutes:", remaining_minutes)

"""Explanation:

If the input is 135:
- Hours = 135 // 60 → 2
- Remaining minutes = 135 % 60 → 15
"""

# 5. Write a program that takes a three-digit number and calculates the sum of its digits using arithmetic operators.

num = int(input("Enter a three-digit number: "))

first_digit = num // 100  # Explanation: Extracts the first digit of the number.
middle_digit = (num // 10) % 10  # Explanation: Extracts the middle digit of the number.
last_digit = num % 10  # Explanation: Extracts the last digit of the number.

total = first_digit + middle_digit + last_digit  # Explanation: Adds all three digits together.

print("Sum of digits:", total)

# 6. Write a program that takes a number as input and checks whether it is divisible by both 3 and 5 using the modulus operator.

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:  # Explanation: Checks whether the number is divisible by both 3 and 5.
    print("It is divisible by both 3 and 5.")  # Explanation: Displays the message if both conditions are true.
else:
    print("It is not divisible by both 3 and 5.")  # Explanation: Displays the message if either condition is false.

# 7. Write a program that takes a total number of students and a group size as input. Calculate how many complete groups can be formed and how many students remain.

no_student = int(input("Enter the number of students: "))
team = int(input("Enter the group size: "))

formed = no_student // team  # Explanation: Calculates the number of complete groups.
remaining = no_student % team  # Explanation: Calculates the number of students remaining.

print(formed)
print(remaining)

# 8. Write a program that takes the base and height of a triangle as input and calculates its area.

b = float(input("Enter the base: "))
h = float(input("Enter the height: "))

area = 0.5 * b * h  # Explanation: Multiplies base and height by 0.5 to calculate the triangle's area.

print(area)  # Explanation: Displays the calculated area.

# 9. Write a program that takes a number as input and calculates its square, cube, and fourth power using the exponentiation operator.

num = int(input("Enter a number: "))

square = num ** 2  # Explanation: Raises the number to the power of 2.
cube = num ** 3  # Explanation: Raises the number to the power of 3.
fourth = num ** 4  # Explanation: Raises the number to the power of 4.

print(square)
print(cube)
print(fourth)

# 10. Write a program that takes a total number of seconds as input and converts it into hours, minutes, and remaining seconds.

sec = int(input("Enter the total seconds: "))

hours = sec // 3600  # Explanation: Calculates the complete hours.
minutes = (sec // 60) % 60  # Explanation: Calculates the remaining minutes after extracting hours.
remaining = sec % 60  # Explanation: Calculates the remaining seconds.

print("Hours:", hours)
print("Minutes:", minutes)
print("Remaining seconds:", remaining)


""" Assignment Operators — 10 Questions
Operators: =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, <<=, >>=
"""

# 1. Create a variable balance with an initial value of 1000. Add 500 to it using an assignment operator and display the updated balance.

balance = 1000
balance += 500  # Explanation: Adds 500 to the current balance and updates it.
print(balance)  # Explanation: Displays the updated balance.            # output: 1500

# 2. Create a variable score with an initial value of 80. Subtract 15 from it using an assignment operator and display the result.

score = 80
score -= 15  # Explanation: Subtracts 15 from the current score and updates it.
print(score)  # Explanation: Displays the updated score.                    # output: 65

# 3. Create a variable price with an initial value of 250. Multiply it by 3 using an assignment operator and display the result.

price = 250
price *= 3  # Explanation: Multiplies the current price by 3 and updates it.
print(price)  # Explanation: Displays the updated price.                # output: 750

# 4. Create a variable number with an initial value of 50. Divide it by 4 using an assignment operator and display the result.

number = 50
number /= 4  # Explanation: Divides the current number by 4 and updates it.
print(number)  # Explanation: Displays the updated number.              # output: 12.5

# 5. Create a variable number with an initial value of 29. Use an assignment operator to store the remainder when it is divided by 5.

number = 29
number %= 5  # Explanation: Stores the remainder when number is divided by 5.
print(number)  # Explanation: Displays the remainder.           # output: 4

# 6. Create a variable number with an initial value of 27. Use floor division assignment to divide it by 4 and display the result.

number = 27
number //= 4  # Explanation: Divides number by 4 and stores the floor division result.
print(number)  # Explanation: Displays the updated number.          # output: 6

# 7. Create a variable number with an initial value of 3. Use exponentiation assignment to raise it to the power of 4.

number = 3
number **= 4  # Explanation: Raises number to the power of 4 and updates it.
print(number)  # Explanation: Displays the result.      # output: 81

# 8. Create a variable number with an initial value of 12. Use the bitwise AND assignment operator with 10 and display the result.

number = 12
number &= 10  # Explanation: Performs bitwise AND with 10 and stores the result.
print(number)  # Explanation: Displays the result.      # output: 8

"""Explanation:
  1100   (12)
& 1010   (10)
------
  1000   (8)
"""

# 9. Create a variable number with an initial value of 5. Use the bitwise OR assignment operator with 3 and display the result.

number = 5
number |= 3  # Explanation: Performs bitwise OR with 3 and stores the result.
print(number)  # Explanation: Displays the result.      #output: 7

"""Explanation:
  0101   (5)
| 0011   (3)
------
  0111   (7)
"""


# 10. Create a variable number with an initial value of 8. Use the right shift assignment operator to shift its bits one position to
#  the right. Display the result.

number = 8
number >>= 1  # Explanation: Shifts the bits one position to the right.
print(number)  # Explanation: Displays the result.      # output: 4

"""Explanation:
Before: 1000  (8)
After:  0100  (4)
"""

""" Comparison Operators — 10 Questions
Operators: ==, !=, >, <, >=, <="""

# 1. Write a program that takes two numbers as input and checks whether they are equal or not using a comparison operator.

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print(x == y)  # Explanation: Checks whether both numbers are equal and displays True or False.

# 2. Write a program that takes two numbers as input and displays the greater number. If both numbers are equal, display a message saying they are equal.

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if x > y:
    print(f"{x} is the greater number")  # Explanation: Displays x if it is greater than y.
elif x < y:
    print(f"{y} is the greater number")  # Explanation: Displays y if it is greater than x.
else:
    print("Both numbers are equal")  # Explanation: Displays a message if both numbers are equal.


# 3. Write a program that takes a person's age as input and checks whether the person is at least 18 years old.

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")

# 4. Write a program that takes a student's marks as input and checks whether the student has scored 40 or more marks.

marks = int(input("Enter the marks: "))

if marks >= 40:
    print("Student has passed")
else:
    print("Student has low score")


# 5. Write a program that takes a number as input and checks whether it is not equal to zero.

x = int(input("Enter a number: "))

print(x != 0)  # Explanation: Checks whether x is not equal to zero.


# 6. Write a program that takes a person's age as input and checks whether their age is between 18 and 60, including both limits. 
# Use comparison operators.

x = int(input("Enter your age: "))

if x >= 18 and x <= 60:
    print("Age is between 18 and 60")
elif x < 18:
    print("Minor")
else:
    print("Older")


# 7. Write a program that takes the prices of two products as input and checks whether the first product is cheaper than the second.

x = int(input("Enter the first product price: "))
y = int(input("Enter the second product price: "))

if x < y:
    print("First product is cheaper than the second")
else:
    print("First product is not cheaper than the second")

# 8. Write a program that takes a number as input and checks whether it is greater than or equal to 100.

x = int(input("Enter a number: "))

if x >= 100:
    print("Number is greater than or equal to 100")
else:
    print("Number is less than 100")

# 9. Write a program that takes a username as input and checks whether it is equal to "admin".

x = input("Enter a username: ")

print(x == "admin")  # Explanation: Checks whether the entered username matches "admin".


# 10. Write a program that takes three numbers as input and uses comparison operators to determine the largest number. 
# Handle cases where two or more numbers are equal.

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if x == y == z:
    print("All three numbers are equal")

elif x >= y and x >= z:
    print("x is the largest number")

elif y >= x and y >= z:
    print("y is the largest number")

else:
    print("z is the largest number")


""" Logical Operators — 10 Questions
Operators: and, or, not"""

# 1. Write a program that takes a person's age as input and checks whether they are at least 18 and at most 60 years old.

age = int(input("Enter your age: "))

if age >= 18 and age <= 60:
    print("Eligible")
else:
    print("Not eligible")

# 2. Write a program that takes a student's marks as input and checks whether the marks are between 40 and 100, inclusive.

marks = float(input("Enter your marks: "))

if marks >= 40 and marks <= 100:
    print("Passed")
else:
    print("Failed")

# 3. Write a program that takes a person's age and citizenship status as input. Check whether the person is at least 18 and is a citizen. 
# Use a Boolean variable for citizenship.

age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")

is_citizen = citizen == "yes"

if age >= 18 and is_citizen:
    print("Person is eligible")
else:
    print("Not eligible")

# 4. Write a program that takes a number as input and checks whether it is divisible by either 3 or 5.

num = int(input("Enter a number: "))

if num % 3 == 0 or num % 5 == 0:
    print("Passed")
else:
    print("Failed")

# 5. Write a program that takes a username and password as input. Allow access only when the username is "admin" and the password is "python123".

name = input("Enter a username: ")
password = input("Enter a password: ")

if name == "admin" and password == "python123":
    print("Login successful")
else:
    print("Error: Incorrect username or password")



# 6. Write a program that takes a person's age as input and uses not to check whether the person is under 18.

age = int(input("Enter your age: "))

if not age >= 18:
    print("Under 18")  # Explanation: Displays this if the person is under 18.
else:
    print("18 or older")  # Explanation: Displays this if the person is 18 or older.

# 7. Write a program that takes a day of the week as input. Display "Weekend" if the day is Saturday or Sunday; otherwise, display "Weekday".

day = input("Enter a day of the week: ")

if day == "Saturday" or day == "Sunday":
    print("Weekend")  # Explanation: Displays Weekend if the day is Saturday or Sunday.
else:
    print("Weekday")  # Explanation: Displays Weekday for all other days.

# 8. Write a program that takes a number as input and checks whether it is outside the range of 10 to 50. Use the not operator to
#  reverse the condition that checks whether the number is within the range.

num = int(input("Enter a number: "))

if not (num >= 10 and num <= 50):
    print("Number is not in range")  # Explanation: Displays this if the number is below 10 or above 50.
else:
    print("Number is in range")  # Explanation: Displays this if the number is between 10 and 50, including both limits.

# 9. Write a program that takes a student's marks in three subjects as input. Check whether the student has scored at least 40 in every subject.

subj1 = int(input("Enter marks for subject 1: "))
subj2 = int(input("Enter marks for subject 2: "))
subj3 = int(input("Enter marks for subject 3: "))

if subj1 >= 40 and subj2 >= 40 and subj3 >= 40:
    print("Student has passed all subjects")  # Explanation: Displays this if every subject has at least 40 marks.
else:
    print("Student has failed")  # Explanation: Displays this if at least one subject has less than 40 marks.

# 10. Write a program that takes a person's age and membership status as input. Allow a discount if the person is under 18 or has a
#  valid membership. Use or to combine the conditions.

age = int(input("Enter your age: "))
member = input("Are you a member? (yes/no): ")

is_member = member == "yes"  # Explanation: Checks whether the person has membership and stores True or False.

if age < 18 or is_member:
    print("Discount allowed")  # Explanation: Allows a discount if the person is under 18 or has membership.
else:
    print("Discount not allowed")  # Explanation: Displays this if neither condition is true.


""" Identity Operators 
Operators: is, is not

Important: Identity operators check whether two variables refer to the same object, not whether their values are equal.

For these exercises, use lists, variables, and None where appropriate.
"""
# 1. Create a list called numbers containing five integers. Assign it to another variable called another_numbers. Use is
# to check whether both variables refer to the same list.

numbers = [1, 2, 3, 5, 4]

another_numbers = numbers  # Explanation: Assigns the same list object to another variable.

print(numbers is another_numbers)  # Explanation: Checks whether both variables refer to the same object.

# output: True

# 2. Create two separate lists containing the same three numbers. Use is and == to check their identities and values.

number = [1, 2, 3]
another_number = [1, 2, 3]

print(number is another_number)  # Explanation: Checks whether both variables refer to the same object.
print(number == another_number)  # Explanation: Checks whether both lists contain the same values.

# output: False
# output: True

# 3. Create a variable called name and assign None to it. Use is to check whether name is None.

name = None  # Explanation: Assigns the special None value to name.

print(name is None)  # Explanation: Checks whether name refers to None.

## output: True

# 4. Create a variable called result and assign None to it. Use is not to check whether result is not None.

result = None  # Explanation: Assigns the special None value to result.

print(result is not None)  # Explanation: Checks whether result does not refer to None.

## output: False

# 5. Create a list called fruits and assign it to another variable called my_fruits. Change an item through my_fruits and 
# demonstrate that the change is visible through fruits. Use is to verify their identity.

fruits = ['apple', 'banana', 'orange']

my_fruits = fruits  # Explanation: Both variables refer to the same list.

my_fruits[1] = 'watermelon'  # Explanation: Changes the second item in the shared list.

print(fruits)  # Explanation: Displays the changed list through fruits.
print(my_fruits)  # Explanation: Displays the changed list through my_fruits.

print(fruits is my_fruits)  # Explanation: Checks whether both variables refer to the same object.

""" output:
['apple', 'watermelon', 'orange']
['apple', 'watermelon', 'orange']
True 

Explanation: The change made through my_fruits is reflected in fruits because both variables refer to the same list object.
Because my_fruits = fruits does not create a new list. Both variables refer to the same list object.

So, when you change an item through my_fruits, the change is also visible through fruits."""

# 6. Create a list called original and make a separate copy called copied using the list's .copy() method. Use is and == to 
# check whether the lists are the same object and whether their contents are equal.

original = ['book', 'pen']

copied = original.copy()  # Explanation: Creates a separate copy of the original list.

print(original is copied)  # Explanation: Checks whether both variables refer to the same object.
print(original == copied)  # Explanation: Checks whether both lists contain the same values.

## output:
# False
# True

# 7. Write a program that takes a name as input. If the variable is None, display "Name is missing". Otherwise, display the name.
# Use an identity operator for the check.

name = input("Enter a name: ")

if name is None:
    print("Name is missing")  # Explanation: Displays this if name is None.
else:
    print(f"{name}")  # Explanation: Displays the entered name.

# 8. Create a list called first_list and assign it to second_list. Then create a third, separate list with the same contents. Use
#  identity operators to compare the three variables.

first_list = ['animal', 'bird', 'butterfly']

second_list = first_list  # Explanation: Refers to the same list as first_list.
third_list = second_list.copy()  # Explanation: Creates a separate list with the same contents.

print(first_list is second_list)  # Explanation: Checks whether both refer to the same object.
print(first_list is third_list)  # Explanation: Checks whether they refer to the same object.
print(second_list is third_list)  # Explanation: Checks whether they refer to the same object.

"""output:
True
False
False
"""

# 9. Write a function that returns None when a number is negative and returns the number otherwise. Call the function and use is to 
# check whether the result is None.

def check_number(num):
    if num < 0:
        return None  # Explanation: Returns None if the number is negative.
    else:
        return num  # Explanation: Returns the number if it is zero or positive.

result = check_number(-5)  # Explanation: Calls the function with -5 and stores its result.

if result is None:
    print("Result is None")  # Explanation: Checks whether the returned result is None.
else:
    print(result)  # Explanation: Displays the returned number.

## output:
# Result is None

# 10. Create two variables that refer to the same dictionary. Create a third dictionary with the same key-value pairs. Use is, is
#  not, and == to compare the dictionaries.

first = {"name": "John", "age": 25}

second = first  # Explanation: Both variables refer to the same dictionary.

third = {"name": "John", "age": 25}  # Explanation: Creates a separate dictionary with the same key-value pairs.

print(first is second)  # Explanation: Checks whether both refer to the same object.
print(first is third)  # Explanation: Checks whether they refer to the same object.
print(first is not third)  # Explanation: Checks whether they refer to different objects.
print(first == third)  # Explanation: Checks whether both dictionaries contain the same values.

## output:
# True
# False
# True      
# True

""" Membership Operators — 10 Questions
Operators: in, not in"""

# 1. Create a list of five fruits. Take a fruit name as input and check whether it exists in the list using in.

fruits = ['apple', 'banana', 'cherry', 'orange', 'melon']

fruit = input("Enter a fruit name: ")

print(fruit in fruits)  # Explanation: Checks whether the entered fruit exists in the fruits list.

"""output:
Enter a fruit name: apple
True"""

# 2. Create a string containing a sentence. Take a word as input and check whether that word exists in the sentence.

sentence = "Python is a popular programming language"

word = input("Enter a word: ")

print(word in sentence)  # Explanation: Checks whether the entered word exists in the sentence.

"""output:
Enter a word: popular
True"""