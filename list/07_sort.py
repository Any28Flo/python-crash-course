# We could sort our list
guests_list = []

guests_list.append('Ned')
guests_list.append('Sansa')
guests_list.append('Arya')

# sorted() -> Temporarily
print(sorted(guests_list))

print(guests_list)

# sort() -> sort the list permanently
guests_list.sort()

print(guests_list)
guests_list.sort(reverse=True)

print(guests_list)

# print the list in reverse

cars = ["bwm", "toyota", "audi", "subaru"]

cars.reverse()
print(cars)
cars.reverse()
print(cars)
