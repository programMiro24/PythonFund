sequence_of_numbers = list(map(int, input().split(' ')))
while (command := input()) != 'END':
    command = command.split(' ')
    action = command[0]
    if action == "replace":
        value, replacement = map(int, command[1:])
        index = sequence_of_numbers.index(value)
        sequence_of_numbers[index] = replacement
        continue
    action = command[0] + " " + command[1]
    if action == "find even":
        evens_numbers = list(filter(lambda x: x % 2 == 0, sequence_of_numbers))
        print_numbers = list(map(str, evens_numbers))
        print(' '.join(print_numbers))
        continue
    elif action == "find odd":
        odds_numbers = list(filter(lambda x: x % 2 == 1, sequence_of_numbers))
        print_numbers = list(map(str, odds_numbers))
        print(' '.join(print_numbers))
        continue
    action = command[0] + " " + command[1] + " " + command[2]
    if action == 'add to start':
        numbers = list(map(int, command[3:]))
        sequence_of_numbers = list(numbers + sequence_of_numbers)
    elif action == "remove greater than":
        value = int(command[3])
        sequence_of_numbers = list(filter(lambda x: x <= value, sequence_of_numbers))
    elif action == "remove at index":
        index = int(command[3])
        if 0 <= index < len(sequence_of_numbers):
            sequence_of_numbers.pop(index)
sequence_of_numbers = map(str, sequence_of_numbers)
print(', '.join(sequence_of_numbers))
