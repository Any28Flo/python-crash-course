"""Program to read the json file and print the values"""
from pathlib import Path
import json

# Get the path of  the file
path = Path('famous_dogs.txt')

try:
    # Read the content of the file
    content = path.read_text()

except FileNotFoundError:
    print("File not found")
else:

    # convert to json to string
    famous_dogs = json.loads(content)
    # Print the content
    print(famous_dogs)
