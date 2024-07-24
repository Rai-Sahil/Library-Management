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

    if is_user_in:
        print("You can pick any book")
    else:
        print("Sorry")


main()