"""
Make a list containing a series of short text messages.Pass the list to a function
called show_messages(), which prints each text message.

"""


def show_messages(array_messages):
    for message in array_messages:
        print(message.upper())


messages = ["winter is coming", "fear cuts deeper than swords", "Paint and black", ""]
show_messages(messages)
