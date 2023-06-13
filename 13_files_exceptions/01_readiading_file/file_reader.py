"""In python, we could read data from different files. The steps are :"""
from pathlib import Path

# 1. Read the file path, Path could help us with this task
path = Path('pi_digitis.txt')
# The content of the file is returned as a simple string
content = path.read_text()


# At the end of the string there are a _ blank_space
# To remove this, we coulduse the method rstrip()
# 41 length
print(len(content.rstrip()))

# Also we could chain the outputs

path_chaining = Path('pi_digitis.txt').read_text().rstrip()
print(path_chaining)
