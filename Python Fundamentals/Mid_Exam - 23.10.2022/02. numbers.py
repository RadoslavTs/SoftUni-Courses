list_of_numbers = list(map(int, input().split()))
command = input()
while command != "Finish":
    command_list = command.split()
    action = command_list[0]
    if action == "Add":
        number_to_add = int(command_list[1])
        list_of_numbers.append(number_to_add)
    elif action == "Remove":
        number_to_remove = int(command_list[1])
        list_of_numbers.remove(number_to_remove)
    elif action == "Replace":
        value_to_find = int(command_list[1])
        replacement_value = int(command_list[2])
        if value_to_find in list_of_numbers:
            value_index = list_of_numbers.index(value_to_find)
            list_of_numbers[value_index] = replacement_value
    elif action == "Collapse":
        value_to_collapse = int(command_list[1])
        temp_list = []
        for item in list_of_numbers:
            if item >= value_to_collapse:
                temp_list.append(item)
        list_of_numbers.clear()
        for item in temp_list:
            list_of_numbers.append(item)
    command = input()
string_list = list(map(str, list_of_numbers))
print(" ".join(string_list))