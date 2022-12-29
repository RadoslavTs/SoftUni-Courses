input_line = input().split()
command = input()
resulting_list = input_line.copy()
while command != "3:1":
    command = command.split()
    command_first = command[0]
    command_second = int(command[1])
    command_third = int(command[2])
    resulting_word = ""
    if command_first == "merge":
        for sequence in range(command_second, command_third+1):
            if sequence >= len(resulting_list):
                continue
            else:
                resulting_word += resulting_list[sequence]
        del resulting_list[command_second:command_third+1]
        if resulting_word != "":
            resulting_list.insert(command_second, resulting_word)
    elif command_first == "divide":
        word_to_change = resulting_list[command_second]
        word_length = len(word_to_change)
        inserting_index_one = command_second
        if word_length % command_third == 0:
            deletable = word_length // command_third
            deletable_length = int(word_length / deletable)
            del resulting_list[command_second]
            last_change = 0
            last_second_index = deletable
            for sequence_two in range(deletable_length):
                resulting_word = word_to_change[last_change:last_second_index]
                if resulting_word != "":
                    resulting_list.insert(inserting_index_one, resulting_word)
                    inserting_index_one += 1
                last_change += deletable
                last_second_index += deletable
        else:
            del resulting_list[command_second]
            delete_value = len(word_to_change) // command_third
            inserting_index = command_second
            for sequence_three in range(command_third):
                if sequence_three +1 == command_third:
                    resulting_word = word_to_change
                    resulting_list.insert(inserting_index, resulting_word)
                else:
                    resulting_word = word_to_change[0:delete_value]
                    resulting_list.insert(inserting_index, resulting_word)
                    word_to_change = word_to_change[delete_value:]
                    inserting_index += 1
    command = input()
resulting_string = " ".join(resulting_list)
print(resulting_string)
