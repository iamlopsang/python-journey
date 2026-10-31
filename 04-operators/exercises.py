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
print(balance)  # Explanation: Displays the updated balance.

# 2. Create a variable score with an initial value of 80. Subtract 15 from it using an assignment operator and display the result.

score = 80
score -= 15  # Explanation: Subtracts 15 from the current score and updates it.
print(score)  # Explanation: Displays the updated score.

# 3. Create a variable price with an initial value of 250. Multiply it by 3 using an assignment operator and display the result.

price = 250
price *= 3  # Explanation: Multiplies the current price by 3 and updates it.
print(price)  # Explanation: Displays the updated price.

# 4. Create a variable number with an initial value of 50. Divide it by 4 using an assignment operator and display the result.

number = 50
number /= 4  # Explanation: Divides the current number by 4 and updates it.
print(number)  # Explanation: Displays the updated number.


