prompt = "\n Tell something, and I will repeat it back to you: "
prompt += "\n Enter quit to end the program. "
flag = True
while flag:
    message = input(prompt)
    if message == 'quit':
        flag = False
    else:
        print(message)
