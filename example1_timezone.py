# Author: Lasalosi Kaifa
# Example 1: Current time of a timezone using pytz module

from datetime import *          # Import everything from datetime module
import pytz                     # Import pytz for timezone handling

# Create a timezone object for India (Kolkata)
tz_INDIA = pytz.timezone('Asia/Kolkata')

# Get current datetime in India timezone
datetime_INDIA = datetime.now(tz_INDIA)

# Print the India time formatted as HH:MM:SS
print("INDIA time:", datetime_INDIA.strftime("%H:%M:%S"))

#The actual time will vary depending on when you run it

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