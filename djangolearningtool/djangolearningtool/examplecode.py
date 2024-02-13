# This document covers various topics such as variables, data types, input/output, conditional statements, loops, functions, 
# lists, tuples, dictionaries, classes, file handling, exception handling, modules, regular expressions, multithreading, virtual
#  environments, and third-party libraries. Each topic is explained with examples to aid your understanding. Feel free to experiment 
# with the code and modify it as needed to deepen your understanding of Python. Happy learning!

"""
Python Learning Document

This document covers various Python topics with extensive example code.
"""

# Topic: Variables and Data Types

# Variables
name = "Alice"
age = 30
is_student = False

# Data Types
string_variable = "Hello, World!"
integer_variable = 42
float_variable = 3.14
boolean_variable = True
list_variable = [1, 2, 3, 4, 5]
tuple_variable = (1, 2, 3)
dictionary_variable = {'key1': 'value1', 'key2': 'value2'}

# Topic: Basic Input/Output

# Output
print("Hello, World!")

# Input
name = input("Enter your name: ")
print("Hello,", name)

# Topic: Conditional Statements

# If-else statement
x = 10
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Topic: Loops

# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Topic: Functions

# Function definition
def greet(name):
    print("Hello,", name)

# Function call
greet("Alice")

# Topic: Lists

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying elements
my_list[0] = 6

# Iterating over a list
for item in my_list:
    print(item)

# Topic: Tuples

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  # Output: 1

# Immutable nature
# my_tuple[0] = 6  # This will raise an error

# Iterating over a tuple
for item in my_tuple:
    print(item)

# Topic: Dictionaries

# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'is_student': False}

# Accessing elements
print(my_dict['name'])  # Output: Alice

# Modifying elements
my_dict['age'] = 31

# Iterating over a dictionary
for key, value in my_dict.items():
    print(key, value)

# Topic: Classes and Objects

# Class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello,", self.name)

# Object creation
person = Person("Alice", 30)

# Accessing attributes
print(person.name)  # Output: Alice

# Calling methods
person.greet()

# Topic: File Handling

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Topic: Exception Handling

# try-except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

# Topic: Modules and Packages

# Importing modules
import math

# Using functions from modules
print(math.sqrt(25))  # Output: 5.0

# Creating and using custom modules
# Example: Create a module named mymodule.py with a function add(a, b) which returns the sum of two numbers.
# import mymodule
# print(mymodule.add(5, 3))  # Output: 8

# Topic: Regular Expressions

import re

# Matching a pattern
pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
text = "Contact us at alice@example.com"
match = re.search(pattern, text)
if match:
    print("Email found:", match.group())

# Topic: Multithreading

import threading

# Define a function for the thread
def print_numbers():
    for i in range(5):
        print(i)

# Create two threads as follows
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Start the threads
thread1.start()
thread2.start()

# Join the threads to wait until they finish
thread1.join()
thread2.join()

# Topic: Virtual Environment

# Creating a virtual environment
# $ python -m venv myenv

# Activating a virtual environment (Windows)
# $ myenv\Scripts\activate

# Activating a virtual environment (Unix/Linux)
# $ source myenv/bin/activate

# Deactivating a virtual environment
# $ deactivate

# Topic: Third-Party Libraries

# Example: Installing and using the requests library
# $ pip install requests
# import requests
# response = requests.get("https://api.example.com/data")
# print(response.json())

# Conclusion
print("Congratulations! You've completed the Python Learning Document.")
