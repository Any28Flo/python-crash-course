"""
Pets: Make several dictionaries, where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner's name.
Store these dictionaries in a list called pets. Next, loop through your list
and as you do, print everything you know about each pet.

"""
pets = []
sasha = {
    'breed': 'dog',
    'color': ['black', 'white'],
    'owner': 'erika'
}
mishi = {
    'breed': 'cat',
    'color': ['brown', 'black'],
    'owner': 'beli'
}
hercules = {
    'breed': 'dog',
    'color': ['white'],
    'owner': 'mike'
}
pocochip ={
    'breed': 'dog',
    'color': ['black', 'white'],
    'owner': 'paps'
}
pets.append(sasha)
pets.append(mishi)
pets.append(hercules)
pets.append(pocochip)

for pet in pets:
    print(pet)
    print(f"The breed  is a {pet['breed']}")
    for key, value in pet.items():
        if key == 'owner':
            print(f"The {key} is :{value.title()}")
        if key == 'color':
            print(f"The color is  {key}: {value} ")
       # print(f"The breed  {key}: {value} ")