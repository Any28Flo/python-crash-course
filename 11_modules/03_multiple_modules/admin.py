"""A class that can be used to represent an Admin"""

from user import User


class Privilege:
    """A simple attemp to model privileges"""

    def __init__(self, name):
        self.name = name


class Admin(User):
    """A simple attempt to model a Admin"""

    def __init__(self, first_name, last_name, nick_name, privileges):
        """Initialize attributes to represent an Admin"""
        super().__init__(first_name, last_name, nick_name)
        self.privileges = privileges

    def add_privilege(self, privilege):
        """Append a privilege to privileges"""
        self.privileges.append(privilege)

    def print_privilege(self):
        """Print the array to privileges"""
        for privilege in self.privileges:
            print(privilege.name)
