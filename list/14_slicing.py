players = ["charles", "martina", "michel", "florence", "eli"]

print(players[0:3])

# If you omit the first index in a slice. Python automatically starts your
# slice at the beginning of the list
print(players[:4])

print(players[2:])

print(players[-3:])
# You can use a slice in a for loop if you want to loop through a subset of
# elements in a list
for item in players[:3]:
    print(item.title())
# Iterate by the end
for item in players[-3:]:
    print(item)

# Coping  a list
my_food = ["pizza", "falafel", "cake"]
# copy a list
friend_food = my_food[:]
print(friend_food)