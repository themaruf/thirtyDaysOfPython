# Print Hello World!
print("Hello World!")

# Variables (Primitive Data Structures)
# Integer
age = 35
# Float
height = 76.8
# String
name = "Jhon Doe"
# Boolean
is_male = True

print(name)
print(age)
print(height)
print(is_male)

# Strings
phrase = "Hello"
print(phrase.upper())
print(phrase.lower())
print(len(phrase))
print(phrase[0]) # prints H
print(phrase.index("H")) # prints 0
print(phrase.replace("lo", "p"))

#Numbers
print(10 % 4)
my_num = -11;
print(str(my_num) + " is my favourite number.")
print(abs(my_num))
print(pow(3,2))
print(max(4,6))
print(min(4,6))
# print(round(3.7))

from math import *

print(floor(3.8))
print(sqrt(64))

# Get inputs from user
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + " years old!")

# Create a very basic calculator
num1 = input("Enter a number: ")
num2 = input("Enter second number: ")

# result = int(num1) + int(num2)
result = float(num1) + float(num2)
print("Sum of "+ num1 + " and " + num2+ " is " + str(result))

# Create Mad Libs game
print("Mad Libs game...")
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter your favourite celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
print("OK. This is a dumb game")


# Lists
numbers = [9, 30, 4, 68, 28, 1]
more_numbers = numbers.copy()
print(more_numbers)

nature = ["Sun", "Moon", "Sky", "Hill"]
nature[3] = "Mountain"
print(nature[0])
print(nature[-1])
print(nature[1:])
print(nature[1:3])

numbers.extend(more_numbers)
nature.append("Mountain")
nature.insert(1, "Earth")
nature.remove("Sky")
nature.pop()
print(nature)
print(nature.index("Earth"))
print(nature.count("Sky"))
nature.clear()

people = [["Maruf", 28], ["Jhon", 38]]
print(people[0][0])

# Tuples (cannot be changed. Like Constants)
coordinates = (90.342, 67.433, 3.4)
print(coordinates[0])
print(coordinates[1])

# Combination of List and Tuple
coordinates = [(90.342, 67.433), (93.2, 63.323)]
coordinates[1] = (60.342, 27.433)

print(coordinates[0])
print(coordinates[1])

combinations = ([1,2], [3,4])
combinations[0][1] = 1
print(combinations)


# Functions
def hello():
    print("Hello!")

def hello_user(first_name, last_name):
    print("Hello " + first_name + " " + last_name)

def cube(num):
    return num * num * num

hello()
hello_user("H M", "Maruf")

print(cube(4))


# If else statement
is_male = False
is_tall = False

if is_male and is_tall:
    print("Person is male and tall")
elif is_male and not(is_tall):
    print("Person is male and not tall")
elif not(is_male) and is_tall:
    print("Person is not male but is tall")
else:
    print("Person is not male and not tall")


# print out maximum number from 3 inputs
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

max_num = max_num(num1, num2, num3)
print(str(max_num) +" is the greatest")