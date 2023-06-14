from pathlib import Path

username = input("What is your name? ")
print(f"Welcome {username}")

path = Path('guest.txt')
path.write_text(f"Welcome {username}")
