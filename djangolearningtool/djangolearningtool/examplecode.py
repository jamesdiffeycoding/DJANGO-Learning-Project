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

# This extended document covers additional Python concepts such as switch statements (implemented using dictionaries),
# optional chaining, different kinds of input fields (string, integer, float, boolean), list comprehensions, lambda functions,
#  generators, and decorators. Each concept is accompanied by example code to help you understand and experiment with the concepts. 
# Feel free to explore and modify the code to deepen your understanding of Python. Happy coding!

"""
Extended Python Learning Document

This document covers various Python concepts with extensive example code.
"""

# Topic: Switch Statements (Using Dictionaries)

def switch_case(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(argument, "Invalid month")

print(switch_case(1))  # Output: January
print(switch_case(13))  # Output: Invalid month

# Topic: Optional Chaining (Python 3.8+)

# Example class with nested attributes
class Address:
    def __init__(self, city):
        self.city = city

class Person:
    def __init__(self, name, address=None):
        self.name = name
        self.address = address

# Creating objects
address = Address(city="New York")
person1 = Person(name="Alice", address=address)
person2 = Person(name="Bob")

# Using optional chaining
print(person1.address.city if person1.address else "Unknown")  # Output: New York
print(person2.address.city if person2.address else "Unknown")  # Output: Unknown

# Topic: Different Kinds of Input Fields

# String Input
name = input("Enter your name: ")
print("Hello,", name)

# Integer Input
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Floating-point Input
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

# Boolean Input
is_student = input("Are you a student? (yes/no): ").lower()
is_student = is_student == "yes"
print("Student Status:", is_student)

# Topic: List Comprehensions

# Generating a list of squares
squares = [x ** 2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtering even numbers
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# Topic: Lambda Functions

# Basic lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Using lambda with map function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Topic: Generators

# Generator function to generate Fibonacci sequence
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
fibonacci_sequence = fibonacci_generator(10)
print(list(fibonacci_sequence))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Topic: Decorators

# Decorator function to log function calls
def logger(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

# Applying the decorator
@logger
def add(a, b):
    return a + b

print(add(3, 5))  # Output: Calling function: add \n 8

# Conclusion
print("Congratulations! You've explored more Python concepts.")

# End of Extended Python Learning Document


# These are some basic code challenges along with their solutions in Python. They cover a range of fundamental concepts including 
# loops, conditionals, strings, lists, and functions. You can use them to practice and deepen your understanding of Python programming.



# Challenge: Calculate the Sum of Digits in a Number
# Write a function that takes an integer as input and returns the sum of its digits.

def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

# Test the function
print(sum_of_digits(123))  # Output: 6 (1 + 2 + 3)


# Challenge: Check if a String is a Palindrome
# Write a function that takes a string as input and returns True if it is a palindrome, False otherwise.

def is_palindrome(string):
    return string == string[::-1]

# Test the function
print(is_palindrome("radar"))  # Output: True


# Challenge: Find the Largest Element in a List
# Write a function that takes a list of numbers as input and returns the largest number in the list.

def find_largest(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Test the function
print(find_largest([1, 5, 3, 9, 2]))  # Output: 9




# Challenge: Count the Number of Words in a Sentence
# Write a function that takes a sentence as input and returns the number of words in the sentence.

def count_words(sentence):
    return len(sentence.split())

# Test the function
# print(count_words("Hello, world!"))  # Output: 2
# Challenge: Check if a Number is Prime
# Write a function that takes a number as input and returns True if it is prime, False otherwise.

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
print(is_prime(7))  # Output: True



