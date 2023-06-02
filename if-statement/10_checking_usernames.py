"""
Do the following to create a program that simulates how websites ensue that everyone has a unique username.
- Make a list of five or more usernames called current_users
- Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the
current_users list.
- Loop through the new_users list to see if each new username has already been used. If a username has not been used,
 print a message saying that the username is available
- Make sure your comparison is case-insensitive. If 'Jhon' has been used, 'JHON' should not be accepted.

"""
current_users = ["cercei", "jhon", "arya", "admin", "sansa", "Jhon"]

new_users = ["homer", "lisa", "arya", "JHON"]


for new_user in new_users:
    if new_user.lower() not in current_users:
        print(f"{new_user.lower()} is available")
    else:
        print(f"{new_user.lower()} is NOT available")


