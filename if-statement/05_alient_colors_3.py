"""
Turn your if-else chain into an if-elseif-else chain.
- If the alien is green, print a message that the player earned 5 points.
- If the alien is yellow, print a message that the player earned 10 points.
- If the alien is red, print a message that the player earned 15 points.
- Write three versions of this program, amking sure each message is printed for the appropiate color alien.

"""
alien_color = input("Insert the alien color: ").lower()
points=0
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
else:
    points = 0

print(f"You earn {points} points")
