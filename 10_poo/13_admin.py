"""
An administrator is a special kind of user. Write a class called Admin that inherits from
the User class you wrote in 04_User.py.
Add an attribute, privileges, that stores a list of strings like "can add a post", "can delete post",
"can ban user", and so on.
Write a method called show_privileges() that lists the administator's set of privileges.
Create an instance of Admin and call your method.

"""


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def descriptive_user(self):
        info = f"The user {self.first_name} has {self.last_name}"
        return info


class Privilege:
    def __init__(self, name):
        self.name = name


class Admin(User):
    def __init__(self, first_name, last_name, privileges=[Privilege('read a post')]):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def add_privilege(self, privilege):
        self.privileges.append(privilege)

    def print_privilege(self):
        for privilege in self.privileges:
            print(privilege.name)


admin_user = Admin('Eri', 'Flores')
admin_user.descriptive_user()
admin_user.print_privilege()
admin_user.add_privilege(Privilege('can add a post'))
admin_user.print_privilege()
