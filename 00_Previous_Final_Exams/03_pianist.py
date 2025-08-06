number_of_pieces = int(input())
pieces = {}
for number_of_piece in range(number_of_pieces):
    piece, composer, key = input().split('|')
    pieces[piece] = {'composer': composer, "key": key}

while (command := input()) != "Stop":
    commands = command.split('|')
    action = commands[0]
    if action == "Add":
        piece, composer, key = commands[1:] # commands[1], commands[2], commands[3]
        if piece not in pieces:
            pieces[piece] = {'composer': composer, "key": key}
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f"{piece} is already in the collection!")
    elif action == "Remove":
        piece = commands[1]
        if piece in pieces:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        piece, new_key = commands[1:]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, data in pieces.items():
    composer = data['composer']
    key = data['key']
    print(f"{piece} -> Composer: {composer}, Key: {key}")
