alien = {'color': 'blue', 'points': 10}

print(alien['color'])
print(alien['points'])

# we could start with an empty diccionary
alien_0 = {}
# and then add some properties
alien_0['color'] = 'blue'
alien_0['points'] = 12

print(alien_0)
# we could modify the values of a dictionary
alien_0['color'] = 'purple'
print(alien_0)

# we could do it more interesting
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(f"original position : {alien_0['x_position']}")

if alien_0['speed'] == 'low':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] += x_increment

print(f"New position : {alien_0['x_position']}")

# we could remove items from a dictionary using the function del
# be careful with function del, because it removes it permanently
# remove color
del alien['color']
print(alien)

# If you are not sure value inside square brackets you could use
# .get method
data_alien = alien.get('color', 'value not set')
print(data_alien)
