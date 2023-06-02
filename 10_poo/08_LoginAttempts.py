"""
Add an attribute called login_attempts to your 04_User.py file.
- Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
- Write another method called reset_login_attempts() that resets the value of login_attemps to 0
- Make an instance of the User class and call increment_login()_attempts() several times. Print the value
of login_attempts to make sure it was incremented, properly,and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0

"""


class User:
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def print_login_attempts(self):
        print(f"Loggin attemps:  #{self.login_attempts}")


mario = User('Mario', 'Bross')
mario.increment_login_attempts()
mario.print_login_attempts()
mario.increment_login_attempts()
mario.print_login_attempts()
mario.reset_login_attempts()
mario.print_login_attempts()