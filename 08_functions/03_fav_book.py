"""
Write a function called favorite_book() that acepts one parameter title,
The function should print a message, such as One of may favorite books is ...
Call the function, making sure to include a book as an argument in the function call
"""


def favorite_book(title):
    # docstring
    """Display favorite book"""
    print(f"One of my favorite book is {title.title()}")


favorite_book("Alice in wonderland")
favorite_book("Games of thrones")
favorite_book("Harry potter")

print(favorite_book.__doc__)