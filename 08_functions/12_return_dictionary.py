"""
We could return almost all data types .
For example dictionaries

"""


def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {
        'first': first_name.title(),
        'last:': last_name.title()
    }
    return person


arya = build_person('Arya', 'Stark')
print(type(arya))
print(arya)
jhon = build_person('Jhon', 'Snow')
print(jhon)
