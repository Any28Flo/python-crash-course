prompt = "\n Tell something, and I will repeat it back to you: "
prompt += "\n Enter quit to end the program. "

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)
