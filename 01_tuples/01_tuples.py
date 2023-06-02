# You can define a tuple with (, )
dimensions = (200, 4)
print(dimensions)
print(type(dimensions))
# We cannot change the value of a tuple
# This  throw an error
#dimensions[0] = 140
# If you would define a tuple with one value you could do it (,)
my_t = (100,)
print(my_t)

# we could loop over all the values in a tuple using a for loop
for dimension in dimensions:
    print(dimension)

# We could overwrite the value of a tuple but not a value
print(f"Original dimension: {dimensions}")
dimensions = (400, 5)
print(f"Modified dimensions: {dimensions}")