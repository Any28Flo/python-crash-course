"""
A keyword argument is when you pass the value as a variable in the function

"""


def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print(f"\nMy favorite animal is a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


# no matter in what order are you passing the arguments
# those are identified by the keyword

describe_pet(animal_type="hamster", pet_name="twilio")
describe_pet(pet_name="sasha", animal_type="dog")
