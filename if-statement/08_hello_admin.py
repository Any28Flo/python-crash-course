"""
Make a list of five or more usernames, including the name 'admin'. Imagine your are writing code
that will print a greeting to each user after they log in to a website. Loop through the list, and print a
greeting to each user.
- If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
- Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
"""

usernames = ["cercee", "jhon", "arya", "admin", "sansa"]

for username in usernames:
    if username != 'admin':
        print(f"Hello {username.title()}, thank you for logging in again.")
    else:
        print(f"Hello {username.upper()}, would you like to see a status report?")

print('End loop usernames!')
