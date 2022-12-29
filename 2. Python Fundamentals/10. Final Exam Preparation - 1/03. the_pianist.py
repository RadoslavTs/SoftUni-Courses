number_of_pieces = int(input())
pieces_dictionary = {}

for piece in range(number_of_pieces):
    input_line = input().split("|")
    composer = input_line[1]
    song = input_line[0]
    song_key = input_line[2]
    song_info = [composer, song_key]
    if song in pieces_dictionary.keys():
        pass
    else:
        pieces_dictionary[song] = song_info
command = input()
while command != "Stop":
    command_split = command.split("|")
    action = command_split[0]
    if action == "Add":
        piece = command_split[1]
        composer = command_split[2]
        key = command_split[3]
        if piece not in pieces_dictionary.keys():
            pieces_dictionary[piece] = []
            pieces_dictionary[piece].append(composer)
            pieces_dictionary[piece].append(key)
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == "Remove":
        piece = command_split[1]
        if piece in pieces_dictionary.keys():
            del pieces_dictionary[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        piece = command_split[1]
        new_key = command_split[2]
        if piece in pieces_dictionary:
            pieces_dictionary[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        pass
    command = input()

for song in pieces_dictionary.keys():
    print(f"{song} -> Composer: {pieces_dictionary[song][0]}, Key: {pieces_dictionary[song][1]}")

