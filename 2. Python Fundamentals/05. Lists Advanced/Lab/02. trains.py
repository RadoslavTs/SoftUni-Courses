wagons = int(input())
train_list = [0 for x in range(wagons)]
command = input()
while command != "End":
    command_list = command.split()
    command_first = command_list[0]
    command_second = int(command_list[1])
    if command_first == "add":
        train_list[-1] += command_second
    elif command_first == "insert":
        command_third = int(command_list[2])
        train_list[command_second] += command_third
    else:
        command_third = int(command_list[2])
        train_list[command_second] -= command_third
    command = input()
print(train_list)
