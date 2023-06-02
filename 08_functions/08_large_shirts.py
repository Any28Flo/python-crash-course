"""
Modify the make_shirt() function so that shirts are large by default
with a message that reads I love python.
Make a large shirt and a medium shirt with the default message , and a shirt of
any size with a different message.

"""


def make_shirt(message='I love python', size='L'):
    print(f"\nMessage: {message.title()}")
    print(f"\nSize: {size.upper()}")


make_shirt()
make_shirt('The things I do for love', 'S')

