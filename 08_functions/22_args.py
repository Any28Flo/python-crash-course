"""
We could send as many arguments as we want
only passing the param
*args
"""


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("Making a pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")


make_pizza('pepperoni')
make_pizza('cheese', 'pineapple', 'beacon')
