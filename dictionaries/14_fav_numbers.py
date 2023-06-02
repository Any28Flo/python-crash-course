"""
Modify your program 03_fav_number.py  so each person can have more than one favorite number.
Then print each person's name along with their favorite numbers.

"""

fav_number = {
    'sansa': [23, 13, 1, 16],
    'arya': [14, 14, 16, 3, 2],
    'rickon': [1, 5, 3],
    'jhon': [9]
}
for person, fav_num in fav_number.items():
    print(f"{person} fav numbers are: ")
    if len(fav_num) > 1:
        for num in fav_num:
            print(f"{num}")
    else:
        print(fav_num)
