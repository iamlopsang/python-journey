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
# 4. Write a program that takes a number of minutes as input and converts it into hours and remaining minutes. Use floor division and modulus.
# 5. Write a program that takes a three-digit number and calculates the sum of its digits using arithmetic operators.
# 6. Write a program that takes a number as input and checks whether it is divisible by both 3 and 5 using the modulus operator.
# 7. Write a program that takes a total number of students and a group size as input. Calculate how many complete groups can be formed and how many students remain.
# 8. Write a program that takes the base and height of a triangle as input and calculates its area.
# 9. Write a program that takes a number as input and calculates its square, cube, and fourth power using the exponentiation operator.
# 10. Write a program that takes a total number of seconds as input and converts it into hours, minutes, and remaining seconds.