# library_system.py

class Book:
    """A base class to represent a generic book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """Represents an electronic book, inheriting from Book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """Represents a physical print book, inheriting from Book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
    
class Library:
    """A class to represent a library, demonstrating composition."""
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        """Adds a book instance to the library's collection."""
        self.books.append(book)
        
    def list_books(self):
        """Prints the details of each book in the library."""
        for book in self.books:
            print(book)


