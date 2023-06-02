"""
Use a variable to represent a person's name and include some whitespace characters
at the beginning and end of the name.
Make sure you use each character combination "\t \n
"""
character = ' jhon show   '
print(f"\t{character}")
print(f"\n{character}")

"""
Print the name once, wo the withespace around the name is displayed.
Then print the name using each of the three stripping funcions
lstring()
rstrip()
strip()
"""
print(character)
print(f"***{character.rstrip()}")
print(f"{character.lstrip()}****")
print(f"{character.strip()}")
