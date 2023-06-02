cars = ["bmw", "audi", "mercedes", "volkswagen"]

for car in cars:
    if car != "bmw":
        print(f"{car.title()}")
    else:
        print(f"{car.upper()}")

requested_toppings = ["mushrooms", "onions", "pineapple"]
# Validate if a value exist in a list or a tuple
isOnions = 'onions' in requested_toppings
print(isOnions)

banned_users = ["carolina", "andrew", "david"]
isBanned = "carlo" not in banned_users
print(isBanned)
