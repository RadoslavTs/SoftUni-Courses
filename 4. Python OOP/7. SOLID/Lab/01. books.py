class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


book_one = Book('The great Gatsby', 'F. Scoot')
book_one.turn_page(50)
book_two = Book('Harry Potter', 'Unknown')
book_two.turn_page(100)

library = Library()
library.add_book(book_one)
library.add_book(book_two)

found_book = library.find_book('Harry Potter')
print(found_book.title)
