"""
Inheritance is when a son class inherance from the father but must follow the next rules:
1) Must be part from the current file
2)
"""


class Car:
    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive(self):
        """ Return a neatly formatted descriptive name """
        long_name = f"{self.year} {self.make} | {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car´s mileage."""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Yoy can't roll ack an odometer")

    def incrementer_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading += mileage
        else:
            print("You can't roll back an odometer")


""" The name of the parent class must be in included in parentheses in the definition of the child class"""


class ElectricCar(Car):

    def __init__(self, make, model, year):
        """super - keyword is a special function that allow us call a method from the parent class"""
        super().__init__(make, model, year)


my_lear = ElectricCar('nissan', 'leaf', 2024)
print(my_lear.get_descriptive())
