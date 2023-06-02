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

    """
    Sometimes you'll want to increment an attribute value by a 
    certain amount, rather than set an entirely new value
    
    """

    def incrementer_odometer(self, mileage):
        if mileage >= 0:
            self.odometer_reading += mileage
        else:
            print("Without privileges")


myNewCar = Car("vmw", "a5", 2023)
myNewCar.update_odometer(15)
myNewCar.read_odometer()
myNewCar.incrementer_odometer(30)
myNewCar.read_odometer()
myNewCar.incrementer_odometer(-20)
myNewCar.read_odometer()