"""
Start with your work from 20_sending_messages.py. Call the function
send_messages() with a copy of the list of messages. After calling
the function, print both of your lists to show that the original list has retained in messages.

"""


def print_messages(message, item):
    print(f"{message} {item}")


def send_messages(array_messages, array_messages_send):
    while array_messages:
        message_send = array_messages.pop()
        print_messages("Sending message...", message_send)
        array_messages_send.append(message_send)


messages_to_send = ["hello", "nice", "start", "dog"]
messages_send = []

send_messages(messages_to_send[:], messages_send)
print("*** MESSAGES SENDED ")
print(messages_send)
