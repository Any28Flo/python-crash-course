from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text().rstrip()

new_language = input("Insert the new string: ")

# splitline -> Split a string into a list.
for item in content.splitlines():
    new_str = item.replace("Python", new_language)
    print(f"{new_str}..")


