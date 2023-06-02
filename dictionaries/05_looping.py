"""
Sometimes we need to loop through the data in a dictionary
We have several options
"""
# looping key and value
fav_languages = {
    'arya': 'python',
    'sansa': 'ruby',
    'jhon': 'c++',
    'rickon': 'javascript',
    'ric': 'javascript'
}
# for key, value in fav_languages.items():
# print(f'\n{key} : {value.title()}')
# looping throw the keys
# for key in fav_languages.keys():
# print(key)
# is the default behavior when looping throw dictionaries, so we can omit the .keys()method
# for name in fav_languages:
# print(name)
user_0 = {
    'username': 'jhon snow',
    'first': 'jhon',
    'last': 'snow'
}
# we could sort the keys of our dictionary and loop throw
print('order')
# for n in sorted(fav_languages.keys()):
# print(n)
# If we only need the values in a dictionary we could use method values()
# print('Print only values')
# for language in fav_languages.values():
#    print(language)
# we could use the method set to print an item unique
for language in set(fav_languages.values()):
    print(language)
