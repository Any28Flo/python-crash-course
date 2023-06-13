from pathlib import Path

path = Path('pi_digitis.txt')
content = path.read_text()

lines = content.splitlines()

for line in lines:
    print(line)
