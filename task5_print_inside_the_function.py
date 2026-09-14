# Author: Lasalosi Kaifa
# Example 1: Print inside the function

# Initialize a global counter
registration_counter = 50000

def student_registration():
    global registration_counter  # Use the global counter

    # Generate the Registration ID using the current counter value
    registration_id = registration_counter
    registration_counter += 1  # Increment the counter for the next registration

    date = input("Enter the registration date (dd/mm/yyyy): ")
    student_id = input("Enter the Student ID: ")
    student_name = input("Enter the Student Name: ")
    course_name = input("Enter the Course Name: ")

    # Display the information
    print("\nPrinting Student Registration Information:")
    print(f"Date: {date}")
    print(f"Student ID: {student_id}")
    print(f"Student Name: {student_name}")
    print(f"Course Name: {course_name}")
    print(f"Registration ID: {registration_id}")

# Call the function:
student_registration()

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