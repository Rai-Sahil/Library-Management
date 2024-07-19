class Users():
    database = {"Sahil": "1234"}

    def sign_in(self, username, password):
        if self.database.get(username) == password:
            print("User is in")
            return True
        else:
            if self.database.get(username):
                print("User not found")
            else:
                print("Password is incorrect")
            return False

    def sign_up(self, username, password):
        if username in self.database:
            print("User already exists. User not added.")
        else:
            self.database[username] = password
            print("User successfully added.")