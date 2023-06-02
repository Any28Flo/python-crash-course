"""
Write a function called city_country() that takes in the name of a city
and its conutry. The function should return a string formatted like this

********
"Santiago, Chile"
********

Call your function with at least three city-country pairs, and print the values that are returned

"""


def city_country(city, country):
    return f"{city}, {country}"


paris = city_country('paris', 'francia')
print(paris)
roma = city_country('roma', 'italia')
print(roma)
guadalajara = city_country('guadajara', 'jalisco')
print(guadalajara)
