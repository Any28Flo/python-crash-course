from pathlib import Path

files = ['cats.txt', 'dogs.txt', 'cat_dogs.txt']
icon = '🐶'


def read_file(path):
    """Function to read files"""
    try:
        content = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        return content


for file in files:
    print(f"{file}: \n")
    value = read_file(file)
    try:
        lines = value.splitlines()
    except AttributeError:
        pass
    else:
        if file == 'dogs.txt':
            icon = '🐶'
        else:
            icon = '🐱🐈'
        for line in lines:
            print(f"{line} {icon}")

    print(f" \n")
