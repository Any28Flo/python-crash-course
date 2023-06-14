from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()

str_replace = input("Insert the new string to replace")

for item in content.rstrip().splitlines():
    new_str = item.replace('Python', str_replace)
    print(f"{new_str}")
