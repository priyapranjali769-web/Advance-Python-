class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"ID: {self.book_id}, Title: {self.title}, Status: {status}")


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"Patron '{patron.name}' registered successfully.")

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print(f"Book '{book.title}' borrowed successfully.")
                else:
                    print("Book is already borrowed.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print(f"Book '{book.title}' returned successfully.")
                else:
                    print("Book was not borrowed.")
                return
        print("Book not found.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            book.display()


# Main Program
library = Library()

library.add_book(Book(101, "Python Basics"))
library.add_book(Book(102, "Data Structures"))

library.register_patron(Patron(1, "Pranjali"))
library.register_patron(Patron(2, "Aman"))

library.display_books()

library.borrow_book(101)
library.display_books()

library.return_book(101)
library.display_books()