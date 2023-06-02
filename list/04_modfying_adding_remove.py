# We can modify an item from a list

# We could do using the index of the element an replace his value

motorcycles = ["Ducati", "Honda", "Italika"]
# Before change
print(motorcycles)
# After change
motorcycles[0] = "Yamaha"
print(motorcycles)

# We could add a item to our list with two ways
# 1. append the item to the tail of the list
motorcycles.append("Vento")
print(motorcycles)
# 2. Specifying the index of the new element
motorcycles.insert(1, "Torino")
print(motorcycles)

# We could remove items from 2 ways
# 1. Delete it. You can no longer access the value that was removed
# You must know the index of the item to delete
del motorcycles[1]
print(motorcycles)
# 2. Pop the element. The pop method remove the element from the list but you could work
# with that item after removing it.
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
