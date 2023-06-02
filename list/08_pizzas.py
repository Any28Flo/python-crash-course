"""
Think f at least three kinds of your favorite pizza. Store these pizza names in a list,
and then use a for loop to pint the name of each pizza.
"""
fav_pizzas = ["hawaiana", "peperoni", "cheese"]

for pizza in fav_pizzas:
    print(f"{pizza}")


# Modify your for loop to print a sentence using the name of the pizza, instead of printing just the
# name of the pizza. For each pizza, you should have one line of output
# containing a simple statement like I like ...

for pizza in fav_pizzas:
    print(f"I like {pizza.title()} pizza\n")
print("I really love pizza")
# Add a line at the end of your program, outside the for loop, that states how much you like pizza.
# The output should consist of three or mor lines about the kinds of pizza you like and then an additional
# Sentence, such as I really love pizza




