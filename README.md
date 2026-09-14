# IT5016_Assessment-3_20267040
PracticePracticePractice

-----------------------------------------------------------------------------------------------

# Example 1: Current time of a timezone using pytz module
## Code Explanation
# Imports `datetime` and `pytz`
# Creates a timezone object for `Asia/Kolkata`
# Gets the current datetime in that timezone
# Formats and prints it as HH:MM:SS

## Status
# Correct – requires `pytz` to be installed.

## Notes
# If you get `ModuleNotFoundError: No module named 'pytz'`, install it with pip
# You can change `'Asia/Kolkata'` to any valid timezone string (e.g., `'Pacific/Auckland'`)

## Key Principles:
# SRP (Single Responsibility Principle): Mostly followed, but I/O and logic are mixed.
# KISS (Keep It Simple, Stupid): Simple and direct.
# Improvement: Extract to a function; avoid wildcard imports.

-----------------------------------------------------------------------------------------------

# Task 1 - Simple Function
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

Task 1 - Modified greeting
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

Task 1 - Welcome message and addition
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

-----------------------------------------------------------------------------------------------

# Example 1: Print inside the function
## Code Explanation
# Declares a global counter `registration_counter` starting at 50000
# Defines `student_registration()` which uses the global counter
# Assigns the current counter value to `registration_id` then increments it
# Prompts the user for date, student ID, student name, and course name
# Prints all collected info plus the unique Registration ID inside the function

## Status
# Correct – works as intended, but I/O and logic are mixed inside the function.

## Notes
# The `global` keyword is required to modify `registration_counter` inside the function.
# Each call to `student_registration()` produces a unique Registration ID (50000, 50001, ...).
# If you need to reuse the data elsewhere, returning it would be more flexible.

## Key Principles:
# SRP (Single Responsibility Principle): Not fully followed – the function collects, generates, and prints.
# KISS (Keep It Simple, Stupid): Simple and easy to follow.
# Improvement: Extract printing to outside the function; return the collected data.

-----------------------------------------------------------------------------------------------

Activity 1: Inventory Management System
## Code Explanation
# Imports `datetime` for consistency (though not used in this prototype)
# Defines global `item_id_counter` and `inventory` dictionary for data persistence
# `add_inventory_item`: Prompts for name, quantity, price with validation; generates unique ID; stores in dictionary; returns details
# `calculate_total_value`: Calls `add_inventory_item`; calculates Quantity × Price; displays and returns total value
# `update_inventory`: Checks if ID exists; prompts for new quantity and price with validation; updates dictionary; returns success message
# `display_inventory_item`: Checks if ID exists; retrieves and displays all item details including calculated total value
# Main block demonstrates all four tasks in sequence

## Status
# Correct – requires no external modules beyond standard library

## Notes
# Input validation uses `try/except` to handle non-numeric entries for Quantity and Price
# Global variables ensure data persists between function calls as required
# Item ID counter increments automatically with each new item added
# You can modify the starting counter value or initial inventory as needed

## Key Principles:
# SRP (Single Responsibility Principle): Each function handles one specific task (add, calculate, update, display)
# KISS (Keep It Simple, Stupid): Simple dictionary storage and straightforward logic
# Improvement: Could separate I/O from logic further; could use classes for better encapsulation

-----------------------------------------------------------------------------------------------

# Activity 1: Simple Banking System
## Code Explanation
# Defines three classes: `Account`, `Customer`, and `Transaction`
# `Account` handles balance logic (deposit, withdraw, display_balance)
# `Customer` links a name to an `Account` and displays combined info
# `Transaction` routes a deposit/withdraw request to the correct `Account` method
# The test block creates one account, one customer, and two transactions

## Status
# Correct - runs with no external dependencies (pure standard Python).

## Notes
# The actual balance values will vary depending on the transactions you run.
# You can add more transactions by creating new `Transaction` objects.
# For persistence, balances could be saved to a file or database later.

## Key Principles:
# SRP (Single Responsibility Principle): Each class has one clear job
#   (Account = money, Customer = identity, Transaction = action routing).
# KISS (Keep It Simple, Stupid): Simple, readable methods with no over-engineering.
# Improvement: Add input validation (reject negative amounts) and an
#   `if __name__ == "__main__":` guard for cleaner test separation.

-----------------------------------------------------------------------------------------------

# Example 2: Class with Dictionary Storage and Static Method for ID Generation
## Code Explanation
# Defines a `StudentRecord` class holding a single attendance entry
# Defines an `AttendanceSystem` class that stores records in a dictionary
# IDs are generated automatically via `_generate_id()` starting at 1001
# `to_tuple()` demonstrates tuple usage when displaying records
# `run_demo()` provides a scripted example instead of user input

## Status
# Correct – runs as a standalone script with no external dependencies.

## Notes
# Dictionary lookup by student ID is faster than linear search in a list
# Average returns 0.0 when no records exist, avoiding division by zero
# Update arguments are keyword-friendly (can pass one or both)

## Key Principles:
# SRP (Single Responsibility Principle): StudentRecord handles data; AttendanceSystem manages records.
# KISS (Keep It Simple, Stupid): Dictionary storage keeps lookup clean and direct.
# Improvement: Could add a menu-driven interface like Example 1 and file persistence.
