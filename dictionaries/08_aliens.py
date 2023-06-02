# list of dictionary
aliens = []
for alien in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in range(10):
    new_alien = {'color': 'yellow', 'points': 10, 'speed': 'medium'}
    aliens.append(new_alien)

for alien in range(10):
    new_alien = {'color': 'red', 'points': 15, 'speed': 'fast'}
    aliens.append(new_alien)

for alien in aliens:
    print(f"\n {alien}")
