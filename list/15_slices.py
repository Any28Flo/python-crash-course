"""
Using one of the programs you wrote in this chapter, add several lines to the end of the program
that do the following.
- Print the message "thr first three items in the list are. Then use a slice to print the
first items from that program's list.
- Print the message "three items from the middle of the list are:" Then use a slice to print three
items from the middle of the list
- Print the message "The last three items in the list are: " Then use a slice to print the last three items in
the list

"""
animals = ["dog", "cat", "bird", "bison", "fox", "camel", "beluga wale" ]
print("The first three elements in animals array")

for animal in animals[:3]:
    print(animal)

print("\n Three items from the middle of the list are: ")
print(animals[2:5])

print("\n The last three items in the animal list are: ")
print(animals[4:])