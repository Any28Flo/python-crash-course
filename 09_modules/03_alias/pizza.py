

def make_pizza(size, *toppings):
    print(f"Make a pizza {size}:")
    print(f"The toppings are:")
    for topping in toppings:
        print(f"-{topping}")
