"""
PYTHON has a removesuffix method that works exactly like removeprefix. Assign the value
python_notes.txt to a variable called filename. Then use the removesuffix() to display the filename
without the file extension. like some file browsers do
"""
filename = 'python_notes.txt'
filename = filename.removesuffix('.txt')
print(filename)

starch_url = 'https://nostarch.com'
starch_url = starch_url.removeprefix('https://')
print(starch_url)