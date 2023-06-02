"""
Start with your program 15_album.py.
Write while loop that allows users to enter an album's artist and title.
Once ou have that information, call make_album with the user's input and print the
dictionary that's created. Be sure to include a quit value in the while loop
"""


def make_album(artist_name, album_title):
    album_info = {
        'artist': artist_name,
        'album': album_title
    }
    return album_info


user_albums = []

while True:
    print('\nPlease insert album info')
    print('Insert "q" to quit the program ')

    artist_name = input('Artist name: ')
    if artist_name == 'q':
        break

    album_name = input('Album name: ')
    if album_name == 'q':
        break
    new_album = make_album(artist_name, album_name)
    user_albums.append(new_album)


#for album in user_albums:
#    for item,value in album.items():
#        print(f"arti")

for album_info in user_albums:
    for key,value in album_info.items():
        if key == 'artist':
            print(f"{key} : {value}")
        else:
            print(f'{key}: {value.upper()}')
    print('\n')

