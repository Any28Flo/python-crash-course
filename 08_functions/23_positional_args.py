"""
We could pass as many arguments as we want
The only rule for this is pass the *args at last
"""


def make_pizza(size, *toppings):
    print(f"Make a pizza {size}:")
    print(f"The toppings are:")
    for topping in toppings:
        print(f"-{topping}")


make_pizza('Small', 'cheese', 'peperonit', 'mushrooms')
make_pizza('Family', 'peperoni')
