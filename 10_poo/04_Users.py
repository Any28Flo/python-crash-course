"""
Make a class called User. Create two attributes called first_name and last_name, and then create several
other attributes that are typically stored in a user profile.
Make a method called describe_user()  that print a summary of the user´s information. Make another
method called greet_user() that print a personalized greeting to the user
Create several instances representing different users, and call both methods for each user.

"""


class User:
    def __init__(self, first_name, last_name, age, points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.points = points

    def describe_user(self):
        print(f"The user {self.first_name} {self.last_name} has the next info:"
              f"Has {self.age} and has {self.points} points")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}  welcome to the JUNGLE")

    def print_points(self):
        print(self.points)


mario = User('mario', 'bross', 12, 12)
mario.describe_user()
luigi = User('luigi', 'bross', 12)
luigi.describe_user()
luigi.greet_user()
luigi.print_points()