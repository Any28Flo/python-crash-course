from pathlib import Path
import json

"""Program to save data in json format """

famous_dogs = ['snoppy', 'scooby-do', 'jack-dog']
# The name of our file
file = Path('famous_dogs.txt')
# Convert our data to json
contents = json.dumps(famous_dogs)
# write the content
file.write_text(contents)
