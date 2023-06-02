"""
The arguments could be optional, for this
we define this values lastly
"""


def print_full_name(first_name, last_name, second_name=''):
    if second_name:
        full_name = f"{first_name.title()} {second_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"

    return full_name


print(print_full_name('Khal', 'Drogo'))
print(print_full_name('Asha', 'Greyjoy'))
print(print_full_name('Eddard',  'Stark', '"Ned"'))
