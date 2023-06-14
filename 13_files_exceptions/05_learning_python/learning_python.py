from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
lines = content.splitlines()
items = []

for line in lines:
    print(line)
    items.append(line)

print(items)
