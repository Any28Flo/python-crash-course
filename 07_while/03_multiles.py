"""
Ask the user for a number, and then report whether the number is a multiple
of 10 or not.
"""
number = int(input("Enter a nuber: "))
if number % 10 == 0:
    print("Number is multiple of 10")
else:
    print("Number is NOT multiple")