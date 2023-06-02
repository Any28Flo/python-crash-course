"""
Imagine an alien was just showdown in a game. Create a variable called alien_color
and assign it a value of 'green' , 'yellow', or 'red'.
- Write an if statement to test whether the alien's color is green. If it is, print a message
that the player just earned 5 points.
- Write one version of this program that passes the if test and another that fails.

"""
alien_color = input('Assign a value (green, yellow or red) : ')
points = 0
if alien_color.lower() == 'green':
    points += 5
else:
    points += 0

print(f'You earn {points} points')

