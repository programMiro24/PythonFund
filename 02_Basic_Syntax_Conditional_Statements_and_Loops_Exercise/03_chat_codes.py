number_of_messages = int(input())
for message in range(number_of_messages):
    message_code = int(input())
    current_messages = ""
    if message_code == 88:
        current_messages = "Hello"
    elif message_code == 86:
        current_messages = "How are you?"
    elif message_code < 88:
        current_messages = "GREAT!"
    else:
        current_messages = "Bye."
    print(current_messages)
