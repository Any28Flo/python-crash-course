flag = True

# while flag:
print('Insert "q" to quit')
while flag:

    number_a = input("Insert a number: ")
    if number_a == 'q':
        break
    else:
        number_b = input("Insert a number: ")

    try:
        result = int(number_a) + int(number_b)
    except ValueError:
        print("Insert valid numbers")
    else:
        print(result)
        print('**Press "q" to quit')


