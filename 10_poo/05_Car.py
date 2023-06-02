class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    """
    def update_odometer(self, mileage):
        self.odometer_reading  = mileage
    """
    """
    3) Overwrite the method update_odometer
    """

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the
        odometer back
        :param mileage:
        :return:
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


myCar = Car("audi", 'a4', 2024)
print(myCar.get_descriptive())

myCar.read_odometer()

"""
We have different way to update values 
1) Update it directly

"""
myCar.odometer_reading = 25
myCar.read_odometer()

"""
2) Create a method to update the attribute
"""
myCar.update_odometer(15)
myCar.read_odometer()
myCar.update_odometer(7)
myCar.read_odometer()