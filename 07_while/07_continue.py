prompt = "\n Tell something, and I will repeat it back to you: "
prompt += "\n Enter quit to end the program. "
current_number = 0
while current_number <= 5:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

