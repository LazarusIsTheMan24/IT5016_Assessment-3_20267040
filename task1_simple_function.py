# Author: Lasalosi Kaifa
# Task 1 - Simple Function

# Define a function called greet
def greet():
    print("Hello, World!")

# Call the function
greet()

## Code Explanation
# Defines a function `greet()` with no parameters
# Prints a fixed greeting message when called
# The function is invoked once at the bottom

## Status
# Correct – runs without any external dependencies.

## Notes
# Change the string inside `print()` to display a different message
# The function must be called after it is defined

## Key Principles:
# SRP (Single Responsibility Principle): Followed – the function only prints a greeting.
# KISS (Keep It Simple, Stupid): Very simple and direct.
# Improvement: Accept a name parameter to make it reusable.

# Task 1 - Modified greeting
def greet():
    print("Welcome to IT5016!")

# Call the function
greet()

## Code Explanation
# Same structure as Example 1, but the printed text is changed
# Demonstrates that function behaviour can be updated by editing the body

## Status
# Correct – runs without any external dependencies.

## Notes
# The output changes each time you edit the string
# Useful for testing that your edits are actually being executed

## Key Principles:
# SRP (Single Responsibility Principle): Followed – only responsible for the greeting.
# KISS (Keep It Simple, Stupid): Minimal and clear.
# Improvement: Pass the message as an argument for flexibility.

# Task 1 - Welcome message and addition

# Define a function that adds two integers defined inside it
def add_numbers():
    a = 5
    b = 10
    print(f"The sum of {a} and {b} is {a + b}")

# Display welcome message first
print("Welcome to the program!")

# Call the function to display the addition result
add_numbers()

## Code Explanation
# `add_numbers(a, b)` takes two parameters and returns their sum
# Two calls are made with integers and floats respectively
# Results are stored and printed

## Status
# Correct – runs without any external dependencies.

## Notes
# Works with both integers and floats
# Returning a value makes the function reusable elsewhere

## Key Principles:
# SRP (Single Responsibility Principle): Followed – only performs addition.
# KISS (Keep It Simple, Stupid): Minimal and clear.
# Improvement: Add type hints (e.g., `a: float, b: float`) for clarity.