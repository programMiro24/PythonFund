password_string = input()

while(command := input()) != 'Done':
    command = command.split(' ')
    action = command[0]
    if action == 'TakeOdd':
        password_string = password_string[1::2]
        print(password_string)
    elif action == 'Cut':
        index, length = map(int, command[1:])
        password_string = password_string[:index] + password_string[index + length:]
        print(password_string)
    elif action == "Substitute":
        substring, substitute = map(str, command[1:])
        if substring in password_string:
            password_string = password_string.replace(substring, substitute)
            print(password_string)
        else:
            print("Nothing to replace!")

print(f'Your password is: {password_string}')
