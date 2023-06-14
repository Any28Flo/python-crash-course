from pathlib import Path

hobbies = ''

for item in range(0, 4):
    new_hobbie = input("What is your favorite hobbie? ")
    hobbies += new_hobbie + "\n"

print(hobbies)

path = Path('hobbies.txt')
path.write_text(hobbies)