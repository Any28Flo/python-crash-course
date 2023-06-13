"""Python program to read a file and work with it as a string """
from pathlib import Path

# Get the file path
path = Path('pi_digitis.txt')
# Read the file content
content = path.read_text()
# splitlines ->Split a string into a list where each line is a list item
lines = content.splitlines()

# iterate throw ecah line of the list
pi_string = ''
for line in lines:
    pi_string += line
# print the new string

print(pi_string)
print(f'length {len(pi_string)}')

# If we want to remove of the blank spaces we could use the
# lstrip -> Remove blank spaces to the left of the string

string_pi = ''
for line in lines:
    string_pi += line.lstrip()

print(string_pi)
print(f'length {len(string_pi)}')