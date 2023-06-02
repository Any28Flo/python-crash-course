"""
write a program that asks the user how many people are in their dinner group.
If the answer is more than eight, print a message saying they'll have to wait for table.
Otherwise, report that their table is ready.
"""
people_group = int(input("How many people are in their dinner group: "))

if people_group > 8:
    print("You must wait for table")
else:
    print("Your table is ready")

