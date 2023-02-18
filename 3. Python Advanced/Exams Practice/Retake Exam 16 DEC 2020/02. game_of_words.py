input_string = input()
size = int(input())
field = []
player_position = []

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for _ in range(size):
    input_line = list(input())
    field.append(input_line)
    if "P" in input_line:
        player_position = [_, input_line.index("P")]
field[player_position[0]][player_position[1]] = '-'
command_number = int(input())
for sequence in range(command_number):
    command = input()
    new_row, new_col = player_position[0] + directions[command][0], player_position[1] + directions[command][1]
    if 0 <= new_row < len(field) and 0 <= new_col < len(field):
        player_position = [new_row, new_col]
        letter = field[new_row][new_col]
        if letter != '-':
            input_string += letter
            field[new_row][new_col] = '-'
    else:
        input_string = input_string[:-1]

field[player_position[0]][player_position[1]] = 'P'

print(input_string)
for _ in field:
    print(''.join(_))