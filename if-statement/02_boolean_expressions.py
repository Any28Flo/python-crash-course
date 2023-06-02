"""
Write a series of conditional tet. Print a statement describing each test
and your prediction for the results of each test and your prediction for the
results of each test. Your code should look something like this:
"""
car = "subaru"
print("Is car == 'subaru'  ? I predict True.")
print(car == 'subaru')
print("\n Is car == 'audi'? I predict False.")
print(car == 'audi')

password = '09871'
print('Is password == "09871"? I predict True.')
print(password == '09871')

# test using the lower method
username = "Erika002"
print('Is username == "erika002"? I predict True')
print(username.lower() == 'erika002')

# numerical test involving equality and inequality, greater than, less than
age = 18

print('Is age > 18? I predict True')
print(age >= 18)
print('Is age < 18? I predict False')
print(age < 18)

# Test using the and keyword and the or keyword
print(f"and :{age > 0 and age < 18}")

print(f"or : {age >= 18 or age > 25 }")
# Test whether an item is in a list
characters = ["cercei", "snow", "kira"]
character = input('Character to search :')
is_snow_in_list = character.lower() in characters
print(f"{character} is in list: {is_snow_in_list}")
# Test whether an item is not in a list
banned_users = ["bluemoon", "montero", "jaramillo"]
user = input('What is your user name: ')
is_banned = user is not banned_users
print(f"{user} - {is_banned} - is not banned user:")
