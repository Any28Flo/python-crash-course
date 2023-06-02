"""
Make a dictionary containing three major rivers and the country each river runs through.
- Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
- Use a loop to print the name of each river ncluded in the dictionary,
- Us a loop to print the name of each country included in the dictionary.

"""
principal_rivers = {
    'nile': "Runts through Medierranean and it's 7088 length",
    'amazon': "Runts through Brazil, Peru, Bolivia and it's 6,992 length",
    'yangtze': "Runts through China and it's 6,418 length",
    'mississippi': "Runts through Canada and it's 6,275 length",
    'yenisei': "Runts through Russia  and it's 5,539 length",
}
# - Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for river, value in principal_rivers.items():
    print(f"\n{river.title()} : {value}")

# - Use a loop to print the name of each river included in the dictionary,
for river in principal_rivers.keys():
    print(f"\n{river.title()}")

#- Use a loop to print the name of each country included in the dictionary.
for description in principal_rivers.values():
    print(f"{description}")
