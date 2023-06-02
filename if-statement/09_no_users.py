"""
Add an if test 08_hello_admin.py to make sure the list of users is not empty.
- If the list is empty, print the message We need to find some users!
- Remove all  the usernames from your list, and make sure the correct message is printed.
"""
usernames = []
if usernames:
    print(usernames)
else:
    print("We need to find some users!")
