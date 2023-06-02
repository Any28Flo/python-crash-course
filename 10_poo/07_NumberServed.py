"""
Start with your program 03_Restaurant.py.
- Add an attribute called number_serverd with a default value of 0. Create an instance called restaurant from this class.
Print the number of customers the restaurant has served, and then change this value and print it again.
- Add a method called set_number_served() that lets you set the number of customers
that have been served. Call this method with a new number and print the value again.
- Add a method called increment_number_served() that lets you increment the number of customers who've been served. Call this
method with any number you like that could represent how may customers were server in, say, a day of business.

"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def print_number_customers(self):
        print(f"The number of customers are {self.number_served}")

    def set_number_served(self, num_customers):
        if num_customers > 0:
            self.number_served = num_customers
        else:
            print("You can't roll back the number of customers")

    def increment_number_served(self, num_customers):
        if num_customers > 0:
            self.number_served += num_customers
        else:
            print("You can't roll back the number of customers")


myRestaurant = Restaurant('Pollos hermanos', 'mexican food')
myRestaurant.print_number_customers()
myRestaurant.number_served = 12
myRestaurant.print_number_customers()

myRestaurant.set_number_served(23)
myRestaurant.print_number_customers()
myRestaurant.set_number_served(-3)
myRestaurant.print_number_customers()
myRestaurant.increment_number_served(5)
myRestaurant.print_number_customers()
myRestaurant.increment_number_served(-2)
myRestaurant.print_number_customers()
