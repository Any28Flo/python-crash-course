"""
Start with the list you used in 01_names . But instead of printing
each person´s name, print a message to them. The text of each message should be the same,
"""
friends =[ "NeD" , "JoHN", "SANsa", "ArYa" ]
message = "Winter is comming"

for friend in friends:
    print(f" El dicho de {friend.title()} Stark es '{message}'")