collection_of_paintings_numbers = list(map(int, input().split(" ")))

def validate_pictures(painting_1: int, painting_2: int, collect: list) -> bool:
    return painting_1 in collect and painting_2 in collect

def switch(paint_number, paint_number_2, collect):
    if validate_pictures(paint_number, paint_number_2, collect):
        index_1, index_2 = collect.index(paint_number), collect.index(paint_number_2)
        collect[index_1], collect[index_2] = collect[index_2], collect[index_1]

while (command := input()) != "END":
    command = command.split(" ")
    action = command[0]
    if action == "Change":
        painting_number, new_number = map(int, command[1:])
        if painting_number in collection_of_paintings_numbers:
            index = collection_of_paintings_numbers.index(painting_number)
            collection_of_paintings_numbers[index] = new_number
    elif action == "Hide":
        painting_number = int(command[1])
        if painting_number in collection_of_paintings_numbers:
            collection_of_paintings_numbers.remove(painting_number)
    elif action == "Switch":
        painting_number_1, painting_number_2 = map(int, command[1:])
        switch(painting_number_1, painting_number_2, collection_of_paintings_numbers)
    elif action == "Insert":
        index, painting_number = map(int, command[1:])
        if 0 <= index + 1 < len(collection_of_paintings_numbers):
            collection_of_paintings_numbers.insert(index + 1, painting_number)
    elif action == "Reverse":
        collection_of_paintings_numbers.reverse()

sequence_of_paints = list(map(str, collection_of_paintings_numbers))
print(' '.join(sequence_of_paints))
