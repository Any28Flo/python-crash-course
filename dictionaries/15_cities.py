"""
Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
Create a dictionary of information about each city and about that city. The keys for each city's dictionary
 should be something like country, population, and fact.
 Print the name of each city and all of the information you have stored about it.

"""
cities = {
    'barcelona': {
        'footballClub': 'FC Barcelona',
        'population': 1.62,
        'fact': 'Barcelona, the cosmopolitan capital of Spain’s Catalonia region, is known '
                'for its art and architecture.'
    },
    'paris': {
        'footballClub': 'PSG F.C.',
        'population': 2.16,
        'fact': 'France iss capital, is a major European city and a global center'
                ' for art, fashion, gastronomy and culture'
    },
    'Berlin': {
        'footballClub': 'AFC Ajax',
        'population': 3.7,
        'fact': 'Berlin is the only city in the world that has three opera houses holding performances'
    }
}
for city, cityInfo in cities.items():
    print(f"\n {city.title()}")
    fotBallClub = cityInfo['footballClub']
    population = cityInfo['population']
    fact = cityInfo['fact']

    print(f"\t It's football club is {fotBallClub}")
    print(f"\t His populations {population} million")
    print(f"\t A fun fact {fact}")


