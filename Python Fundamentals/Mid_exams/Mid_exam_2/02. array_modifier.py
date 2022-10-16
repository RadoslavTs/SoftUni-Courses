input_list = list(map(int, input().split()))
command = input()
while command != "end":
    command_list = command.split()
    if command_list[0] == "swap":
        swap_index_one = int(command_list[1])
        swap_index_two = int(command_list[2])
        swap_value_one = input_list[swap_index_one]
        swap_value_two = input_list[swap_index_two]
        input_list[swap_index_one] = swap_value_two
        input_list[swap_index_two] = swap_value_one
    elif command_list[0] == "multiply":
        multiply_index_one = int(command_list[1])
        multiply_index_two = int(command_list[2])
        multiply_value_one = int(input_list[multiply_index_one])
        multiply_value_two = int(input_list[multiply_index_two])
        multiply_result = multiply_value_one * multiply_value_two
        input_list[multiply_index_one] = multiply_result
    elif command_list[0] == "decrease":
        counter = 0
        for numbers in input_list:
            resulting_number = int(numbers) - 1
            input_list[counter] = resulting_number
            counter += 1
    command = input()

resulting_list = list(map(str, input_list))
print(", ".join(resulting_list))