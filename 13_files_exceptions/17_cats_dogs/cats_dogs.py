from pathlib import Path

files = ['cats.txt', 'dogs.txt', 'cat_dogs.txt']
icon = '🐶'


def read_file(path):
    try:
        content = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"The file {path}  isn't available")
    else:
        return content


for file in files:
    print(f"{file}: \n")
    value = read_file(file)

    if file == 'dogs.txt':
        icon = '🐶'
    else:
        icon = '🐱🐈'

    for line in value.splitlines():
        print(f"{line} {icon}")

    print(f" \n")
