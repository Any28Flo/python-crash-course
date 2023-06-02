"""A class that can be used to represent a user"""


class User:
    """A simple attempt to model a user"""

    def __init__(self, first_name, last_name, nick_name):
        """Initialize atributes to represent a User"""
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name

    def descriptive_user(self):
        """Return a neatly formatted descriptive name"""
        user_info = f" {self.first_name} {self.last_name} | {self.nick_name}"
        return user_info
