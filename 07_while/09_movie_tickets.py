"""
A movie theater charges different ticket prices depending on a
person's age. If a person is under the age of 3, the ticket is free;
if they are between 3 and 12, the ticket is $10; and if they are over age 12,
the ticket is $15.
Write a while loop in which you ask users ther age, and then tell them the cost of
the movie ticket
"""
prompt = "\n Enter your age. "
prompt += "\n (Enter quit to end the program): "
priceTicket = 0
flag = True
while flag:
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if age < 3:
            priceTicket = 0
        elif age >= 3 and age <= 12:
            priceTicket = 10
        else:
            priceTicket = 15
        print(f"{(f'The ticket cost is ${priceTicket}', 'Your ticket is FREE')[priceTicket == 0]}")
    else:
        flag = False


