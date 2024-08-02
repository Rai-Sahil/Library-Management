from library import library
from user_auth import UsersAuth

def main():
    is_user_in = False

    lib = library()
    lib.add_book(1, "Harry Potter", "J.K. Rowling", "Fiction", "Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling.")
    lib.add_book(2, "The Da Vinci Code", "Dan Brown", "Mystery", "The Da Vinci Code is a 2003 mystery thriller novel by Dan Brown.")

    user_auth = UsersAuth()

    print("Welcome to the library!")
    user_input = int(input("Enter 1 to Sign in\nEnter 2 for sign up\n"))

    if user_input == 1:
        username = input("Enter your new Username\n")
        password = input("Enter new Password\n")
        is_user_in = user_auth.sign_in(username, password)
    elif user_input == 2:
        username = input("Enter you Username\n")
        password = input("Enter Password\n")

        user.sign_up(username, password)
        is_user_in = user_auth.sign_in(username, password)
        print("You were auto signed in.")

    #have 4 options. 1. show book selection 2. borrow book 3. return book 4. sign out
    while is_user_in:
        print("Enter 1 to display book selection\nEnter 2 to borrow a book\nEnter 3 to return a book\nEnter 4 to sign out")
        select = int(input())

        if select == 1:
            lib.print_books()

            
        elif select == 2:
            book_name = input("Enter the name of the book you want to borrow\n")
            if lib.searchBook(book_name) is None:
                print("Book not found")
            elif lib.searchBook(book_name).isTaken:
                print("Book is already taken")
            else:
                lib.searchBook(book_name).bookBorrowed()
                user_auth.addBook(user_auth.getName(), book_name)
                print("Book borrowed")


        elif select == 3:
            book_name = input("Enter the name of the book you want to return\n")
            if lib.searchBook(book_name) is None:
                print("Book not found")
            elif not lib.searchBook(book_name).isTaken:
                print("Book is not taken")
            else:
                lib.searchBook(book_name).bookReturned()
                user_auth.removeBook(user_auth.getName(), book_name)
                print("Book returned")

        elif select == 4:
            is_user_in = False
            print("Signed out")
        else:
            print("Invalid input")


main()