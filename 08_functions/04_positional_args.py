"""
positional arguments
Pass the arguments to some function  based on the order of the arguments
proved.
"""


def describe_pet(animal_type, pet_name):
    """ Display information about pet """
    print(f"\nMy favorite animal is a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('hamster', 'rocky')
