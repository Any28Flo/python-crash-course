from dice import Dice
my_dice = Dice(8)
my_dice.print_side()
value_side = []
number_to_roll = int(input("How many times the dice must roll: "))

for value in range(1, number_to_roll):
    side = my_dice.roll_die()
    value_side.append(side)

print(f"The values are: {value_side}")
