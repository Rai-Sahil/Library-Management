class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def removeBook(self, book):
        self.books.remove(book)

    def getName(self):
        return self.username
    
    