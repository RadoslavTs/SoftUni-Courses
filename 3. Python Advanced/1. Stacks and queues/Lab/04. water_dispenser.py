from _collections import deque

starting_water_quantity = int(input())
name_deque = deque()
start_command = "Start"
break_command = "End"
while True:
    name_input = input()
    if name_input == start_command:
        break
    else:
        name_deque.append(name_input)

while True:
    command = input()
    if command == break_command:
        break
    else:
        if command.isdigit():
            name = name_deque.popleft()
            if starting_water_quantity >= int(command):
                print(f'{name} got water')
                starting_water_quantity -= int(command)
            else:
                print(f"{name} must wait")
        else:
            quantity = int(command.split()[1])
            starting_water_quantity += quantity

print(f"{starting_water_quantity} liters left")




