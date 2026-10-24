# # Assignment 1: Strings

# Q1. Create a string variable containing your name and print it.

name = "Hendry"
print(name)

# Q2. Create a string and print its data type using `type()`.

city = "Kathmandu"
print(city, type(city))

# Q3. Create a string containing your first name and another containing your last name. Join them and print your full name.

first_n = "naruto"
last_n = "uzumaki"

print(first_n + " " + last_n)

# Q4. Store a sentence in a variable and print its length using `len()`.

place = "london"
print(len(place))

# Q5. Create a string containing `"Python Programming"` and print its first character, last character, and fifth character.

x = "Python Programming"

print(x[0])
print(x[17])
print(x[5])


# Q6. Store the string `"Python Programming"` in a variable and print only `"Python"` using slicing.

x = "Python Programming"
print(x[0:6])

# Q7. Create a string containing `"  Hello Python  "` and remove the extra spaces at the beginning and end using `strip()`.

x = "  Hello Python  "
print(x.strip())

# Q8. Store `"python programming"` in a variable and convert all its letters to uppercase and then to lowercase.

x = "Python Programming"
print(x.lower())

# Q9. Create a string containing `"I love Java"` and replace `"Java"` with `"Python"` using `replace()`.

x = "I love Java"
print(x.replace("Java", "Python"))

# Q10. Store `"apple,banana,orange"` in a variable and split the string into a list using `split()`.

x = "apple,banana,orange"
print(x.split(","))


# Q11. Create a string containing `"Python is easy to learn"` and check whether it contains the word `"easy"` using `in`.

x = "Python is easy to learn"

print("easy" in x)

# Q12. Store `"Python123"` in a variable and check whether all its characters are alphanumeric using `isalnum()`.

x = "Python123"

print(x.isalnum())

# Q13. Create a string containing `"Hello World"` and check whether it starts with `"Hello"` and ends with `"World"`.

x = "Hello World"

print(x.startswith("Hello"))
print(x.endswith("World"))

# Q14. Create a variable containing your age as a number and use an f-string to print a sentence displaying your age.

age = int(input("Enter a age:"))
print(f"Your age:{age}")
