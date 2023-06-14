from pathlib import Path

guest = int(input("How many guest do yo wanna have? "))
i = 0
guests = ''
path = Path('guest_book.txt')

while i < guest:
    new_guest = input("What is your name? ")
    guests += 'Welcome to my party ' + new_guest + '\n'
    i += 1

path.write_text(guests)