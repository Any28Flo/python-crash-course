"""
Make a class called Restaurant. The __init__() method for Restaurant should
store two attributes: a restaurant_name, cuisine_type.
Make a methood called open_restaurant() that prints a message incating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually
and then call both methods.
"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, isOpen):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.isOpen = isOpen

    def open_restaurant(self):
        if self.isOpen:
            print(f"The {self.restaurant_name} is OPEN")
        else:
            print(f"The {self.restaurant_name} is CLOSE")

    def desc_restaurant(self):
        print(f"The {self.restaurant_name} has a cuisine type {self.cuisine_type}")


rataTui = Restaurant('Ratatui', 'Itailian food', False)
print(rataTui.restaurant_name)

rataTui.desc_restaurant()
rataTui.open_restaurant()

pollosBrother = Restaurant('Pollos Hermanos', 'mexican food', True)
pollosBrother.desc_restaurant()
pollosBrother.open_restaurant()
print(f"Restaurant name : {pollosBrother.restaurant_name}")

pollosBrotherGreek = Restaurant('Pollos Hermanos', 'geek', False)
print(f"Restaurant {pollosBrotherGreek.restaurant_name}")
pollosBrotherGreek.desc_restaurant()
