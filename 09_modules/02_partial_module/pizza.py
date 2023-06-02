"""
This is a file called "module" here you can define
all the functions you want then import them where its
necessary

"""


def make_pizza(size, *toppings):
    print(f"Make a pizza {size}:")
    print(f"The toppings are:")
    for topping in toppings:
        print(f"-{topping}")
