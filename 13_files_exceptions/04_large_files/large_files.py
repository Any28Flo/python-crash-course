from pathlib import Path

path = Path('pi_million_digits.txt')
content = path.read_text()
lines = content.splitlines()

birthday = input('Enter your birthday, in the form mmddyy: ')

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f'{pi_string[:50]}')
print(len(pi_string))

""" Is your birthday contained in Pi """

if birthday in pi_string:
    print('Your birthday appears in the first milloion digits of pi')
else:
    print('Your birthday NOT appears')

