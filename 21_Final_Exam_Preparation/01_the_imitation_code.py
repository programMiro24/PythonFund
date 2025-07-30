message = input()

while (command := input()) != "Decode":
    parts = command.split('|')
    action = parts[0]
    if action == 'Move':
        number_of_letters = int(parts[1])
        message = message[number_of_letters:] + message[:number_of_letters]
    elif action == 'Insert':
        index = int(parts[1])
        value = parts[2]
        message = message[:index] + value + message[index:]
    elif action == 'ChangeAll':
        substring = parts[1]
        replacement = parts[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
