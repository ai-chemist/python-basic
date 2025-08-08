def show_messages(messages, sent_list):
    """ practice 8-9
    for message in messages:
        print(message)
    """

    while messages:
        message = messages.pop()
        sent_list.append(message)
        print(message)

message_list = ['hello', 'hi', 'bye', 'goodbye']
sent_messages = []

""" practice 8-10
show_messages(message_list, sent_messages)
"""

show_messages(message_list[:], sent_messages)
print(message_list)
print(sent_messages)