"""
number_one = input("Insert a number: ")
number_two = input("Insert a number: ")
"""


def addition(number_one, number_two):
    """Add two numbers"""
    try:
        result = int(number_one) + int(number_two)
    except ValueError:
        print("You must insert a valid number")
    else:
        print(f"The result {number_one}  + {number_two} = {result}")


# Fail test
addition(1, 'a')

# Pass test
addition(3, 5)
