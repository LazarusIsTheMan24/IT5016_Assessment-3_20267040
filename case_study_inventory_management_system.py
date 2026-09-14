# Author: Lasalosi Kaifa
# Activity 1: Inventory Management System

# Global variables to manage inventory state between function calls
item_id_counter = 1000
inventory = {}  # Dictionary to store items by ID for easy lookup and updates

def add_inventory_item():
    """
    Task 1: Prompts for item details, generates a unique ID, 
    stores the item, and returns the item details.
    """
    global item_id_counter
    
    print("\nAdding Inventory Item:")
    item_name = input("Item Name: ")
    
    # Input validation for Quantity
    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")
            
    # Input validation for Price
    while True:
        try:
            price = float(input("Price per Item: $"))
            if price < 0:
                print("Price cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for price.")

    # Generate unique Item ID
    item_id = item_id_counter
    item_id_counter += 1

    # Store item in the inventory dictionary
    inventory[item_id] = {
        "name": item_name,
        "quantity": quantity,
        "price": price
    }

    # Return all inputs along with the generated Item ID
    return item_id, item_name, quantity, price

def calculate_total_value():
    """
    Task 2: Calls add_inventory_item, calculates total value, 
    displays it, and returns the total value.
    """
    # Call Task 1 function to get new item data
    item_id, name, quantity, price = add_inventory_item()
    
    # Calculate total value
    total_value = quantity * price
    
    # Display user-friendly message
    print(f"\nTotal value for {name} (ID: {item_id}): ${total_value:.2f}")
    
    return total_value

def update_inventory(item_id):
    """
    Task 3: Updates quantity and price for a given Item ID.
    Returns a message if the item is not found.
    """
    print("\nUpdating Inventory Item:")
    
    # Check if item exists
    if item_id not in inventory:
        return f"Error: Item ID {item_id} was not found in the inventory."
    
    print(f"Item ID: {item_id}")
    
    # Input validation for new Quantity
    while True:
        try:
            new_quantity = int(input("New Quantity: "))
            if new_quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")
            
    # Input validation for new Price
    while True:
        try:
            new_price = float(input("New Price per Item: $"))
            if new_price < 0:
                print("Price cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for price.")
            
    # Update the inventory dictionary
    inventory[item_id]["quantity"] = new_quantity
    inventory[item_id]["price"] = new_price
    
    return f"Inventory Updated: Item ID {item_id} has been updated to Quantity {new_quantity} and Price ${new_price:.2f}."

def display_inventory_item(item_id):
    """
    Task 4: Displays the details of an inventory item including total value.
    """
    print("\nDisplaying Inventory Item:")
    
    if item_id not in inventory:
        print(f"Error: Item ID {item_id} not found.")
        return
    
    item = inventory[item_id]
    name = item["name"]
    quantity = item["quantity"]
    price = item["price"]
    
    # Calculate Total Value
    total_value = quantity * price
    
    # Format output nicely
    print(f"Item Name: {name}")
    print(f"Item ID: {item_id}")
    print(f"Quantity: {quantity}")
    print(f"Price per Item: ${price:.2f}")
    print(f"Total Value: ${total_value:.2f}")

# --- Example Usage (to demonstrate the functions) ---
if __name__ == "__main__":
    # 1. Add an item and calculate its total value
    print("--- Task 1 & 2 Execution ---")
    total = calculate_total_value()
    
    # 2. Display the item just added (assuming ID 1000)
    print("\n--- Task 4 Execution ---")
    display_inventory_item(1000)
    
    # 3. Update the item
    print("\n--- Task 3 Execution ---")
    update_message = update_inventory(1000)
    print(update_message)
    
    # 4. Display the updated item
    print("\n--- Task 4 Execution (After Update) ---")
    display_inventory_item(1000)
    
    # 5. Try to update a non-existent item
    print("\n--- Task 3 Error Handling ---")
    error_message = update_inventory(9999)
    print(error_message)

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