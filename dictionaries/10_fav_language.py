"""
We could have a dictionary with list inside
"""
fav_languages = {
    'arya': ['python', 'ruby', 'javascript'],
    'cercei': ['c', 'java'],
    'Eddard': ['go', 'perl'],
    'jhon': ['python']
}
for person, languages in fav_languages.items():
    if len(languages) > 1:
        print(f"{person} favorite language are: ")

        for language in languages:
            print(f"\n{language.title()}")
    else:
        print(f"{person} favorite language are: {languages}")

