"""
Choose a color for an alien as you did in exercise
and write an if-ese chain
- If the alien's color is green, print a statement that the player just
earned 5 points for shooting the alien
- If the alien's color isn't green, print a statement that the player just earned 10
point.
- Write one version of this program that runs if block and another that runs the else block.

"""
alien_color = input("Insert alien color: ").lower()
points = 0
if alien_color == 'green':
    points += 5
else:
    points += 10

print(f"You earn {points} points")
