"""
Use the code in fav_languages.py
- Make a list of people who should take the favorite languages poll. Include some
ames that are already in the dictionary and some that are not.
- Loop through the list of people who should take the poll. If ther have already take the poll,
print a message thanking them for responding.
- if they haver not yet taken the poll, print a message inviting them to take the pollk¿
"""
fav_languages = {
    'arya': 'python',
    'sansa': 'ruby',
    'jhon': 'c++',
    'rickon': 'javascript',
    'eddard': 'javascript',

}
fav_languages['bran'] = 'python'
fav_languages['catelyn'] = 'go'
people_take_poll =['arya', 'jhon', 'sansa', 'eddard', 'Daenery']

for key, value in fav_languages.items():
    if key in people_take_poll:
        print(f'{key} fav language is {value.title()}')
    elif key not in people_take_poll:
        print(f"{key.lower()} YOU are NO in the list ")
    else:
        print(f"{key} MUST TO TAKE THE POLL")
