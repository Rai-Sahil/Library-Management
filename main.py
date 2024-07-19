from library import library
from user import User

def main():
    is_user_in = False

    lib = library()
    lib.add_book(1, "Harry Potter", "J.K. Rowling", "Fiction", "Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling.")
    lib.add_book(2, "The Da Vinci Code", "Dan Brown", "Mystery", "The Da Vinci Code is a 2003 mystery thriller novel by Dan Brown.")

    user = User()

    print("Welcome to the library!")
    user_input = int(input("Enter 1 to Sign in\nEnter 2 for sign up\n"))

    if user_input == 1:
        is_user_in = user.sign_in()
    elif user_input == 2:
        user.sign_up()
        is_user_in = user.sign_in()

    if is_user_in:
        print("You can pick any book")
    else:
        print("Sorry")


main()