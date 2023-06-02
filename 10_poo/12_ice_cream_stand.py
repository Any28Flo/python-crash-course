"""
An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from
the Restaurant class you wrote in 03_Restaurant
Either version of the class stores a list of ice cream flavors.
- Write a method that displays these flavors.
- Create an instance of IceCreamStand and call this method.
# restaurant_name, cuisine_type,number_served
"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def get_info(self):
        full_info = f"{self.restaurant_name} | {self.cuisine_type} : {self.number_served}"
        return full_info


class Flavor:
    def __init__(self, name, is_avalaible=False):
        self.name = name
        self.is_avalable = is_avalaible


class IceCreamStan(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served, flavor=[Flavor('mantecado', True)]):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavor

    def print_flavor(self):
        for flavor in self.flavors:
            print(f"{flavor.name} esta { 'existencia ' if flavor.is_avalable else 'no disponible'}")

    def add_flavor(self,name, isAvailable):
        self.flavors.append(Flavor(name, isAvailable))


michoacana = IceCreamStan('la michoacana', 'helados', 0)
print(michoacana.get_info())

new_stan = IceCreamStan('malinali', 'helados', '3')
new_stan.print_flavor()
new_stan.add_flavor('limon', True)
new_stan.add_flavor('nuez', False)
new_stan.print_flavor()