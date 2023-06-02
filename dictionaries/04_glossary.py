"""
Python dictionary can be used to model an actual dictionary. however, to avoid confusion,
let´s call it a glossary.
- Think of five programming words yo´ve learned about in the previos chapters. Use these words
as the keys in your glossary, and store their meanings as values.
- Print each word and its meaning as neatly formatted output. You might print the word followed by
a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line.
Use the new line character to insert a blank line between each word-meaning pair in your output.


"""
glossary = {
    'dictionary': 'collection key-value',
    'tuple': 'list data type but inmutable',

}
# print(f"Dictionary : {glossary['dictionary']}")
# print(f"Tuple: {glossary['tuple']}")

# Replacing the series of print with a loop


# add 5 more python terms to your glossary
glossary['list'] = 'python data type mutable'
glossary['for-in'] = 'method to loop throw list, dictionaries and 01_tuples'
glossary['integer'] = 'python data type to represent integer numbers'
glossary['1_000_000'] = 'we could use _ to represent big numbers'

for k, v in glossary.items():
    print(f"\n {k.title()} : {v} ")
