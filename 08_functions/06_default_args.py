"""
When some parameter is common you could pass it as a default
value

"""


def describe_pet(pet_name, animal_type="dog"):
    """ Display information about pet """
    print(f"\nMy favorite animal is a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# When you use default values, any parameter with a
# default value needs to be listed after all the parameters
# than don't have default values

describe_pet('lady')
describe_pet('Nymeria')
describe_pet('ghost')
describe_pet('mishi', 'gato')