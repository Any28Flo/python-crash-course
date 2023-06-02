"""
Start with a copy of your program from exercise 19_messages.py
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it's printed.
After calling the function, print oth of your list to make sure the messages were moved correctly

"""


def send_message(message, item):
    print(f"{message} : {item}")


def sending_messages(array_messages, array_empty):
    while array_messages:
        message_send = array_messages.pop()
        send_message("item send:", message_send)
        array_empty.append(message_send)


messages_to_send = ["hello", "nice to meet you", "goodbay"]
messages_sended = []

sending_messages(messages_to_send, messages_sended)

print(messages_sended)