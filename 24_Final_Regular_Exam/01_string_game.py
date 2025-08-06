recived_string = input()

while (command := input()) != "Done":
    command = command.split(' ')
    action = command[0]
    if action == "Change":
        character, replacement = command[1:]
        recived_string = recived_string.replace(character, replacement)
        print(recived_string)
    elif action == "Includes":
        substring = command[1]
        is_include = substring in recived_string
        print(is_include)
    elif action == "End":
        substring = command[1]
        is_ending = recived_string.endswith(substring)
        print(is_ending)
    elif action == "Uppercase":
        recived_string = recived_string.upper()
        print(recived_string)
    elif action == "FindIndex":
        character = command[1]
        first_index = recived_string.find(character)
        print(first_index)
    elif action == "Cut":
        start_index, counting = map(int, command[1:])
        recived_string = recived_string[start_index:start_index + counting]
        print(recived_string)

