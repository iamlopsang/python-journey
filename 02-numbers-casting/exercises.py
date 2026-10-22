# ssignment 1: Numbers
# 1. Create an integer variable and a float variable. Print both values and their data types.

x= 10
y= 23.45

print(type(x))
print(type(y))

# 2. Store two numbers in variables and print their sum.

x = 12
y = 15.67

sum = x + y
print("sum of number is :", sum)

# 3. Accept two numbers from the user and display their sum, difference, product, and quotient.

num1 = input("Enter a first number:")
num2 = input("Enter a second number:")
sum= num1 + num2
diff = num1-num2
product = num1 * num2
quotient = num1 /num2

print("sum of the numbers:", sum)
print("difference of the numbers:", diff)
print("product of the numbers:", product)
print("quotient of the numbers:", quotient)

# 4. Accept an integer from the user and print its remainder when divided by 3.

num = int(input("Enter a number:"))
rem= num % 3

print("remainder of the number:", rem)

# 5. Create two variables, a base and an exponent, and print the result using the ** operator.

base = 3
expo = 2

oper = base ** expo
print(oper)

# 6. Accept two integers and display the result of floor division using //.

a = int(input("enter a num1:"))
b = int(input("enter a num2:"))
floor = a//b
print(floor)

# 7. Create a complex number 3 + 5j and print its value and data type

number = 3+5j
print(number)
print(type(number))

# 8. Accept a number from the user and print its absolute value using abs().

a= float(input("enter a number:"))
result = abs(a)
print(result)

# 9. Store 8.7654 in a variable and round it to two decimal places using round().

num = 8.7654
result= round(num, 2)
print(result)

# 10. Create a float variable and use is_integer() to check whether its value represents a whole number.

num = 6.79
result = num.is_integer()
print(result)


        ## Assignment 2: Casting ##
# 11. Convert the float 12.8 to an integer and print the result.

x = 12.8
y = int(x)
print(y)

# 12. Convert the integer 25 to a float and print the result and its data type.

x = 25
y = float(x)
print(y, type(y))

# 13. Convert the string "150" to an integer and print the result and its data type.

price = "150"
pr = int(price)
print(pr, type(pr))

# 14. Convert the string "45.75" to a float and print the result.

s = "45.75"
y = float(s)
print(y, type(y))

# 15. Convert the integer 2026 to a string and print its data type using type().

x = 2026
y = str(x)
print(y, type(y))


# 16. Accept the user's age, convert it to an integer, and print the age five years from now.

age = int(input("Enter your age: "))
age_5 = age + 5
print(age_5)

# 17. Accept two numbers from the user, convert them to integers, and display their sum.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
result = num1 + num2
print(result)

# 18. Accept a decimal number from the user, convert it to a float, and print the number multiplied by 2.

num = float(input("Enter a decimal number: "))
print(num * 2)

# 19. Accept a decimal number, convert it to a float and then to an integer, and print the result of each conversion.

num = input("Enter a decimal number: ")
print(num, type(num))

num = float(num)
print(num, type(num))

num = int(num)
print(num, type(num))

# 20. Convert the integer 7 into a complex number using complex() and print the result and its data type.

x = 7
y = complex(x)
print(y, type(y))

