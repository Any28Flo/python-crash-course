"""

Author: Daedra

This programs uses an exception to read a file and manage if the file exists or not.

"""
from pathlib import Path

path = Path('alice_adventure.txt')

try:
    content = path.read_text(encoding='utf-8')

except FileNotFoundError:
    print(f"The file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    # The content at this moment is a long string
    # Then we use the split method to produce a list of all the words
    words = content.split()
    num_words = (len(words))
    print(f"The file {path} has about {num_words} words.")
