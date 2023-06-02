"""
Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You should have keys such
as first_name, last_name, age and city. Print each piece of information stored in your dictionary.

"""

print(f"first name: { person['first_name']}")
print(f"last name: { person['last_name']}")
print(f"age: { person['age'] }")
print(f"city: { person['city']}")
print(f"house: {person.get('house', 'not set')}")
