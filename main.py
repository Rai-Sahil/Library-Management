class Users():
    database = {"Sahil": "1234"}

    def sign_in(self, username, password):
        if self.database.get(username) == password:
            print("User is in")
        else:
            if self.database.get(username):
                print("User not found")
            else:
                print("Password is incorrect")

    def sign_up(self, username, password):