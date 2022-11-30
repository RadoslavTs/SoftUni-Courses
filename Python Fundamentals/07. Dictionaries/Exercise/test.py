number_of_pieces = int(input())
pieces_dictionary = {}
for sequence in range(number_of_pieces):
    input_line = input().split("|")
    piece = input_line[0]
    composer = input_line[1]
    key = input_line[2]
    if composer in pieces_dictionary.keys():
        if piece not in pieces_dictionary[composer]:
            pieces_dictionary[composer][piece] = key
        else:
            pass
    else:
        pieces_dictionary[composer] = {piece: key}

command = input()
while command != "Stop":
    command_split = command.split("|")
    action = command_split[0]
    if action == "Add":
        piece = command_split[1]
        composer = command_split[2]
        key = command_split[3]
        if composer in pieces_dictionary.keys():
            if piece not in pieces_dictionary[composer]:
                pieces_dictionary[composer][piece] = key
                print(f"{piece} by {composer} in {key} added to the collection!")
            else:
                print(f"{piece} is already in the collection!")
        else:
            pieces_dictionary[composer] = {piece: key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == "Remove":
        piece = command_split[1]
        piece_found = False
        for composing in pieces_dictionary:
            if piece in pieces_dictionary[composing].keys():
                del pieces_dictionary[composing][piece]
                print(f"Successfully removed {piece}!")
                piece_found = True
                break
        if not piece_found:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        piece = command_split[1]
        new_key = command_split[2]
        piece_found = False
        for composing in pieces_dictionary:
            if piece in pieces_dictionary[composing].keys():
                pieces_dictionary[composing][piece] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
                piece_found = True
                break
        if not piece_found:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        pass
    command = input()

for composer, pieces in sorted(pieces_dictionary.items(), key=lambda x: (x[1], x[0])):
    piece = pieces
    who_wrote_it = composer
    # key_value = pieces_dictionary[composer][piece]
    print(f"{piece} -> Composer: {who_wrote_it}")
