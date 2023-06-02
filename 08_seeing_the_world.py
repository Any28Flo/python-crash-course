"""
*** SEEING THE WORLD ***

Think of at least five places in the world you´d like to visit.

-
- Use sort() to change your list so it´stored in reverse-alphabetical order.
print the list to show that its order has changed
"""
# Store the locations in a list. Make sure the list is not in alphabetical order.
places = ["Paris", "Canada", "Cancun", "Puebla", "Roma"]
# Print your list in its original order. Don´t worry about printing the list neatly,
# just print it as a raw Python list.
print(places)

# Use sorted() to print your list in alphabetical order without modifying the actual list.

print(f"ordered: {sorted(places)}")
# Show that your list is still in its original order by printing it
print(f"original: {places}")
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list

print(f"reverse: {sorted(places, reverse=True)}")
# Show that your list is still in its original order by printing it again.
print(f"original {places}")
# Use reverse() to change the order of your list. Print the list to show that its order has changed
places.reverse()
print(f"reverse {places}")
# Use sort() to change your list so it´s stored in alphabetical order.
places.sort()
# Print the list to show that its order has been changed
print(f"order reverse {places}")
print(f"len {len(places)}")
