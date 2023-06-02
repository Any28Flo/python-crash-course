"""A class that can be used to represent a restaurant"""


class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type, is_open=False):
        """Initialize attrihbutes to represent a Restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.is_open = is_open

    def desc_restaurant(self):
        """Return a neatly formatted descriptive name"""
        full_description = f'{self.restaurant_name} - {self.cuisine_type} '
        return full_description.upper()
