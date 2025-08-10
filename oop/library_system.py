class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
    
class Library:
    def __init__(self):
        self._books = {}  # Using dictionary instead of list to store books
        
    def add_book(self, book):
        """Add a book to the library"""
        if not hasattr(self, '_books'):
            self._books = {}
        key = (book.title, book.author)
        self._books[key] = book
        
    def list_books(self):
        """Return a list of all books in the library"""
        return [str(book) for book in self._books.values()]
