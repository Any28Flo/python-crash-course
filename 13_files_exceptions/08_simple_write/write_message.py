from pathlib import Path
path = Path('message.txt')

message = input("Insert the message you wanna send: ")

path.write_text(message)