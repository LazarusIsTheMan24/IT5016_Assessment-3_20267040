# Author: Lasalosi Kaifa
# Activity 1: Simple Banking System

# Step 1: Define the classes

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")


class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def display_customer_info(self):
        print(f"Customer Name: {self.name}")
        self.account.display_balance()


class Transaction:
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.process_transaction()

    def process_transaction(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type!")


# Step 2: Test the functionality

# Creating an account for a customer
account1 = Account(account_number=101, balance=100)
customer1 = Customer(name="Alice", account=account1)

# Display customer details
customer1.display_customer_info()

# Performing transactions
transaction1 = Transaction(account1, 50, "deposit")
transaction2 = Transaction(account1, 30, "withdraw")

# Final account balance
customer1.display_customer_info()

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