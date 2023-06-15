print("Give me two numbers, and I'll divide them")
print("Enter to 'q' to quit ")
flag = True

while flag:
    first_number = input("Insert first number: ")
    if first_number == 'q':
        break
    second_number = input("Insert second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int (second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("Inserta un numero valido")
    else:
        flag = False
        print(answer)
