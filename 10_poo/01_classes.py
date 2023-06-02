
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")


myDog = Dog('Sasha', 3)
# Accessing attributes
print(myDog.name)
print(f'My dog age is {myDog.age}')
# Calling methods
myDog.sit()
myDog.roll_over()