"""
Write  loop that prompts the user to enter a series of pizza toppings until
they enter a 'quit' value. As they enter each topping, print a message saying
you'll add that topping to their pizza
"""
toppings = []

prompt = "\n Enter a topping for your pizza: "
prompt += "\n (Enter quit to end the program) "
topping = ''
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        print(f'I add {topping} to your pizza')

print("Your pizza toppings are:")
for topping in toppings:
    print(f"{topping}")
