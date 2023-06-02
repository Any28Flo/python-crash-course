"""
Write a function called make_shirt() that accepts  size and the
text of a message that should be printed on the shirt. The function should print a sentence
summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt.
Call the function a second time using keyword arguments

"""


def make_shirt(size, message):
    """Print a shirt with size and message params"""
    print(f"Creatin a tshirt size:{size.upper()} "
          f"and the message is : {message.title()}")


make_shirt('m', 'winter is comming')
make_shirt('xl', 'fear cuts deeper than swords')

make_shirt(message='It is not easy to being drunk every day', size='l')
make_shirt(size='s', message='Valar Dohaeris')