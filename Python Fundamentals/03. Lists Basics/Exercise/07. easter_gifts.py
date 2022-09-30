gift_names = input().split()
command = input()
result_string = ""
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
        if index_placement < len(gift_names):
            gift_names[index_placement] = product
        else:
            command = input()
            continue
    else:
        gift_names[-1] = product
    command = input()
for element in gift_names:
    if element == "None":
        gift_names.remove(element)
for result in gift_names:
    result_string += result + " "
print(result_string)