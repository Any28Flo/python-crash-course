"""
Make a dictionary called favorite_places.Think of three names to use as keys in dictionary, and
store one to three favorite places for each person. To make this exercise a bit more interesting,
ask some friends to name afew of their favorite places. Loop through the dictionary, and print each person's
name and their favorite places.

"""
favorite_places = {
    'sansa':[ 'winterfell', 'the iron islands'],
    'Daenerys' : ['acapulco', 'oaxaca'],
    'Eddard' : ['Tlaxcala', 'Guanajuato']
}

for person, places in favorite_places.items():
    print(f'the fav plaves of {person} are:')
    for place in places:
        print(f"\n {place}")
    print("\n")
