"""try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

#2
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

#3
try:
    n = int(input("Enter an integer: "))
    print("Number:", n)

except ValueError:
    print("Invalid input. Please enter a number.")

#4

numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter index: "))
    print(numbers[index])

except IndexError:
    print("Index is out of range")

# 5
student = {
    "name": "Ram",
    "age": 20,
    "mark": 90
}

try:
    key = input("Enter key: ")
    print(student[key])

except KeyError:
    print("Key not found")

# 6

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")
# 7
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

else:
    print("Result:", result)

finally:
    print("Program completed")

# 8
class AgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("Age must be 18 or above")

    print("Eligible")

except AgeError as e:
    print(e)

# 9
try:
    n = int(input("Enter a number: "))

    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

except ValueError:
    print("Invalid input")

# 10
class InvalidMarkError(Exception):
    pass


try:
    mark = int(input("Enter mark: "))

    if mark < 0 or mark > 100:
        raise InvalidMarkError("Mark must be between 0 and 100")

    print("Valid mark")

except InvalidMarkError as e:
    print(e)

except ValueError:
    print("Please enter a number")

"""

""""
#1

with open("data.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("This is file handling.")

print("Data written successfully.")


#2

with open("data.txt", "r") as file:
    data = file.read()

print(data)


#3

with open("data.txt", "a") as file:
    file.write("\nNew data added.")

print("Data appended successfully.")


#4

with open("data.txt", "r") as file:
    lines = file.readlines()

print("Number of lines:", len(lines))


#5

with open("data.txt", "r") as file:
    data = file.read()

words = data.split()

print("Number of words:", len(words))


#6

with open("data.txt", "r") as file:
    data = file.read()

print("Number of characters:", len(data))


#7

with open("data.txt", "r") as source:
    data = source.read()

with open("copy.txt", "w") as destination:
    destination.write(data)

print("File copied successfully.")


#8

word = input("Enter word to search: ")

with open("data.txt", "r") as file:
    data = file.read()

if word in data:
    print("Word found.")
else:
    print("Word not found.")


#9

word = input("Enter word: ")

with open("data.txt", "r") as file:
    for line in file:
        if word in line:
            print(line, end="")


#10

with open("data.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line, end="")


#11

name = input("Enter student name: ")
roll = input("Enter roll number: ")
mark = input("Enter mark: ")

with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Roll No: " + roll + "\n")
    file.write("Mark: " + mark + "\n")

with open("student.txt", "r") as file:
    print(file.read())


#12

import os

filename = input("Enter filename: ")

if os.path.exists(filename):
    print("File exists.")
else:
    print("File does not exist.")


#13

with open("numbers.txt", "r") as file:
    numbers = []

    for line in file:
        numbers.append(float(line.strip()))

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)


#14

with open("data.txt", "r") as file:
    data = file.read()

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in data:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)


#15

with open("file1.txt", "r") as file1:
    data1 = file1.read()

with open("file2.txt", "r") as file2:
    data2 = file2.read()

with open("merged.txt", "w") as file3:
    file3.write(data1)
    file3.write("\n")
    file3.write(data2)

print("Files merged successfully.")
"""