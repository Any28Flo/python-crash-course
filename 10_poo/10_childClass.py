class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        full_name = f"{self.make} {self.model} {self.year}"
        return full_name

    def fill_tank(self):
        print("filling tank")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 50

    def descriptive_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    # Overwrite method from his parent
    def fill_tank(self):
        print("This car doesn't have a gas tank")


my_tsuru = Car('nissan', 'tsuru', 2000)
print(my_tsuru.get_descriptive_name())
my_tsuru.fill_tank()

my_leaf = ElectricCar('nissan', 'leaf', 2004)
print(my_leaf.get_descriptive_name())
my_leaf.descriptive_battery()
my_leaf.fill_tank()
