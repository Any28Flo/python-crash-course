"""
Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method should
check the battery size and set the capacity to 65 if it isn't already. Make an electric car
with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the
battery. You should see an increase in the car's range.

"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        full_info = f"{self.make} , {self.model}   | {self.year}"
        return full_info


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_sizev

    
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
