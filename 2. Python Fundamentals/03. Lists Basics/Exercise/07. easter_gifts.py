gift_names = input().split()
command = input()
while command != "No Money":
    command_list = command.split()
    command = command_list[0]
    product = command_list[1]
    if command == "OutOfStock":
        for sequence in range(len(gift_names)):
            if gift_names[sequence] == product:
                gift_names[sequence] = "None"
    elif command == "Required":
        index_placement = int(command_list[2])
        if 0 <= index_placement < len(gift_names):
            gift_names[index_placement] = product
    elif command == "JustInCase":
        gift_names[-1] = product
    command = input()
while "None" in gift_names:
    gift_names.remove("None")
print(' '.join(gift_names))