"""
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following
- Add a new pizza to the original list
- Add a different pizza to the list friend_pizzas.
- Prove that you have two separate lists. Print the message
    My friend´s favorite pizzas are; and then use for loop to print the second list.
    Make sure each new pizza is stored in the apropiate list.

"""
my_food = ["pizza", "falafel", "cake"]

friend_food = my_food[:]

friend_food.append("ice cream")
my_food.append("coke")

print(f"My favorite food are: {my_food}")
print(f"My favorite friend food are {friend_food}")
