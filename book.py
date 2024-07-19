class Book():

    def __init__(self, ID, name, author, categoryNum, text):
        self.ID = ID
        self.name = name
        self.author = author
        self.categoryNum = categoryNum
        self.text = text
        self.isTaken = False

    def print_book(self):
        print("Name: " + self.name + ", Author: " + self.author + ", Category: " + self.categories[self.categoryNum])

