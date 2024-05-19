def show_messages(short_messages):
    """Print short messages"""
    for message in short_messages:
        print(message)


def send_messages(short_messages, sent_messages):
    """Print sent messages"""

    while short_messages:
        current_message = short_messages.pop()
        print(f"Current message: {current_message}")
        sent_messages.append(current_message)

        print("\nThe following messages were sent out: ")
        for message in sent_messages:
            print(message)


short_messages = ['Hi, there', 'How are you?', 'Good morning', 'Life is great']
sent_messages = []

show_messages(short_messages)

send_messages(short_messages, sent_messages)
print(short_messages)