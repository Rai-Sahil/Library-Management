from typing import Any
from book import Book

class library():

    books = {}

    def add_book(self, ID, name, author, categoryNum, text):
        book = Book(ID, name, author, categoryNum, text)
        self.books[ID] = book

    def removeBook(self, ID):
        del self.books[ID]

    def print_books(self):
        for key in self.books:
            self.books[key].print_book()

    def searchBook(self, name):
        for key in self.books:
            if self.books[key].name == name:
                return self.books[key]
        return None