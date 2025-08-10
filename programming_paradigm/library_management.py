class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False


    
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                return True
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out:
                book.is_checked_out = False
                return True
        return False

    def list_available_books(self):
        available_books =  [book for book in self._books if not book.is_checked_out]
        for book in available_books:
            print(book)