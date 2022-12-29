input_list = list(map(int, input().split()))
command = input()
resulting_list = list(map(int, input_list))
shot_targets = 0
while command != "End":
    command_int = int(command)
    if command_int >= len(input_list):
        command = input()
        continue
    if resulting_list[command_int] != -1:
        removing_value = resulting_list[command_int]
        resulting_list[command_int] = -1
        shot_targets += 1
        sequence = 0
        for number in resulting_list:
            if number == -1:
                sequence += 1
                continue
            else:
                if number > removing_value:
                    result_one = resulting_list[sequence] - removing_value
                    resulting_list[sequence] = result_one
                    sequence += 1
                else:
                    result_two = number + removing_value
                    resulting_list[sequence] = result_two
                    sequence += 1
    command = input()

string_result = list(map(str, resulting_list))
print(f"Shot targets: {shot_targets} -> {' '.join(string_result)}")



