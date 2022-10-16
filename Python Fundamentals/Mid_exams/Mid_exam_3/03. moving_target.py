integer_targets = list(map(int, input().split()))
command = input()
while command != "End":
    command_list = command.split()
    split_command = command_list[0]
    index_value = int(command_list[1])
    power_value = int(command_list[2])
    if split_command == "Shoot":
        if len(integer_targets) > index_value >= 0:
            result = integer_targets[index_value] - power_value
            integer_targets[index_value] = result
            if integer_targets[index_value] <= 0:
                del integer_targets[index_value]
    elif split_command == "Add":
        if len(integer_targets) > index_value >= 0:
            integer_targets.insert(index_value, power_value)
        else:
            print("Invalid placement!")
    elif split_command == "Strike":
        upper_limit = index_value + power_value
        lower_limit = index_value - power_value
        if upper_limit < len(integer_targets) and lower_limit >= 0:
            for sequence in range(upper_limit, lower_limit-1, -1):
                del integer_targets[sequence]
        else:
            print("Strike missed!")
    command = input()

resulting_string_list = list(map(str, integer_targets))
print("|".join(resulting_string_list))


