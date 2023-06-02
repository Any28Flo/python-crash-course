"""
start with the program you wrote 02_person. Make two new dictionaries representing different people,
 and store all three dictionaries
in a list called people. Loop through your list of people.
As you loop through the list, print everything you know about each person.

"""
stark_family = []

jhon = {
    'first_name': 'Jhon',
    'last_name': 'Snow',
    'house': 'stark',
    'quote': '"You have got the North in you. The real North."'
}
rob = {
    'first_name': 'Rob',
    'last_name': 'Stark',
    'house': 'stark',
    'quote': '"All men should keep their word, kings most of all."'
}
eddard = {
    'first_name': 'Eddard',
    'last_name': 'Stark',
    'age': 23,
    'house': 'stark',
    'quote': '"When the snows fall and the white winds blow, the lone wolf dies, but the pack survives."'
}

arya = {
    'first_name': 'Arya',
    'last_name': 'Stark',
    'house': 'stark',
    'quote': 'A girl is Arya Stark of Winterfell, and I am going home."'
}

stark_family.append(jhon)
stark_family.append(rob)
stark_family.append(eddard)
stark_family.append(arya)

for stark in stark_family:
    for key, value in stark.items():
        print(f"{key}: {value}")
    print("\n")

