"""
If you could invite anyone, living or deceased, to dinner, who would you invite?
Make a list that includes at least three people you´d like to invite to dinner.
Then use your list to print a message to each person, inviting then to dinner.

"""
guests_list = []

guests_list.append('Ned')
guests_list.append('Sansa')
guests_list.append('Arya')

message = "Would you like to attend to my dinner on Monday 13"
for guest in guests_list:
    print(f"{message} {guest}?")

# You just heard that one of your guest can´t make the dinner, so you need to
# send out a new set of invitations. You´ll have to think of someone else to invite.
# - Add a print() call at the end , stating the name of the guest who can´t make it
# print(f"Sorry, but {guests_list[1]} can´t attend to our dinner")
# - Modify your list replacing the name of the guest who can´t make it with the name of the new person
# - You are inviting
guests_list[1] = "Jhon Snow"
# Print a second set of invitation messages, one for each person who is still in you list
for guest in guests_list:
    print(f"{message} {guest}?")

# *** MORE GUESTS ***
# You just found a bigger dinner table, so now more space is available. think of three more guests to invite to dinner
# - Add a print call to the end of your program informing people that you found a bigger table
print("Hey folks, I've found a bigger table, I invite someone else")
# - Use insert() to add one new guest to the beginning of your list
# list.insert(pos, elemnt)
guests_list.insert(0, "Brandon Stark")


# - Use insert() to add one new guest to the middle of your list
middle = len(guests_list)

guests_list.insert(int(middle/2), "Theon gray")

# - Use append to add one new guest to the end of your list
guests_list.append( "Rickon Stark")
# - print a new set of invitation messages, one for ach person in your list
for guest in guests_list:
    print(f" {guest}?")

print(guests_list)
print(f"len {len(guests_list)}")

# *** SHRINKING GUEST LIST ***
# You just found out that your new dinner table won´t arrive in time for the dinner,
# and now you have space for only two guests.
# - Add a new line that prints a message saying that you can invite only two people for dinner
print("Sorry guys, I only can invite two of you")
# - Use pop() to remove guest from your list one at a time until only two name remain in your list.
deleted_user = guests_list.pop()
print(deleted_user)
# - Each time you pop a name from your list, print a message to that person letting them know you´re sorry
# you can´t invite them to dinner
# - Print a message to each of the two people still on your list, leating them know they´re still invented

print(f"Sorry {deleted_user} you can't invite to dinner")
deleted_user = guests_list.pop()
print(f"Sorry {deleted_user} you can't invite to dinner")

# - Use del to remove the last two names from your list, so you have an empty list.
print(guests_list)
print(f"len {len(guests_list)}")
del guests_list[-1]
del guests_list[-1]
del guests_list[-1]
del guests_list[-1]

# - Print your list to make sure you actually have an empty list at the end of your program.
