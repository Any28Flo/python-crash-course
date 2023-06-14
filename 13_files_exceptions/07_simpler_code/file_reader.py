from pathlib import Path

content = Path('learning_python.txt').read_text().rstrip().splitlines()

for item in content:
    print(item)
