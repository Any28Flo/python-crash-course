"""
We could return values not only print values
"""


def print_full_name(last_name, first_name):
    return f"{first_name.title()} {last_name.title()}."


men_character = print_full_name('snow', 'jhon')
print(men_character)
fem_character = print_full_name('lanister', 'cercei')
print(fem_character)
