"""
Write a function called describe_City() that accepts the name of
a city and its conuntry. The function should print a simple sentence, such as
Reykjavkik is in Iceland. Give the parameter for the country a default value.
Call your function for threee different cities, at least one of which is not in the
default country.
"""


def describe_city(city="Guadalajara", country='Jalisco'):
    print(f"{city.title()} is in {country.title()}")


describe_city('paris', 'france')
describe_city(country='italy', city='rome')
describe_city(city='Tlaquepaque')
describe_city()
