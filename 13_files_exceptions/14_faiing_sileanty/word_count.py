from pathlib import Path


def word_count(path):
    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # pass statement tells python to do nothing in a block
        pass
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ['alice_adventure.txt', 'little.txt', 'moby_dick.txt',  'siddhartha.txt']

for file in filenames:
    route = Path(f'./files/{file}')
    word_count(route)
