"""
    Composition refers to break our classes into small classes
"""


class Car:
    def __init__(self, year, model, make):
        self.year = year
        self.model = model
        self.make = make

    def get_descriptive_name(self):
        full_name = f"{self.year} {self.make} | {self.model}"
        return full_name


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def get_descriptive_battery(self):
        return f"This car has a {self.battery_size}-km battery"

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 60:
            range = 220

        print(f"This car can go about {range} miles on a full charge")


class ElectricCar(Car):
    def __init__(self, year, model, make):
        super().__init__(year, model, make)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2023)
my_leaf.battery.battery_size = 60
print(my_leaf.battery.get_descriptive_battery())
my_leaf.battery.get_range()
