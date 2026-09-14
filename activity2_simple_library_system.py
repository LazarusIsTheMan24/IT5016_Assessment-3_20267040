# Author: Lasalosi Kaifa
# Activity 2: Simple Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        books = ", ".join([b.title for b in self.borrowed_books]) or "None"
        return f"Member: {self.name} | Borrowed: {books}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member added: {member.name}")

    def borrow_book(self, book_title, member_name):
        book = next((b for b in self.books if b.title == book_title), None)
        member = next((m for m in self.members if m.name == member_name), None)

        if not book:
            print(f"Book '{book_title}' not found.")
            return
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        if book.is_borrowed:
            print(f"Book '{book_title}' is already borrowed.")
            return

        book.is_borrowed = True
        member.borrow(book)
        print(f"'{book_title}' borrowed by {member_name}.")

    def return_book(self, book_title, member_name):
        book = next((b for b in self.books if b.title == book_title), None)
        member = next((m for m in self.members if m.name == member_name), None)

        if not book or not member:
            print("Book or member not found.")
            return
        if book not in member.borrowed_books:
            print(f"{member_name} did not borrow '{book_title}'.")
            return

        book.is_borrowed = False
        member.return_book(book)
        print(f"'{book_title}' returned by {member_name}.")

    def display_books(self):
        print("\n--- Library Books ---")
        if not self.books:
            print("No books in the library.")
        for book in self.books:
            print(book)
        print("---------------------\n")


# ---- Test the functionality ----

library = Library()

# Add books
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

# Add members
library.add_member(Member("Alice"))
library.add_member(Member("Bob"))

# Display all books
library.display_books()

# Borrow and return operations
library.borrow_book("1984", "Alice")
library.borrow_book("1984", "Bob")        # Already borrowed
library.borrow_book("The Great Gatsby", "Bob")

library.display_books()

library.return_book("1984", "Alice")
library.display_books()

# Show member info
print("--- Member Details ---")
for member in library.members:
    print(member)