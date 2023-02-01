matrix = []
matrix_size = 6

for row in range(6):
    matrix.append(input().split())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

current_position = input().split(", ")
current_position = (int(current_position[0][1]), int(current_position[1][0]))

command = input()

while command != "Stop":
    command_split = command.split(', ')
    action = command_split[0]
    direction = command_split[1]
    new_row, new_col = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
    current_position = (new_row, new_col)

    if action == 'Create':
        value = command_split[2]
        if matrix[current_position[0]][current_position[1]] == ".":
            matrix[current_position[0]][current_position[1]] = value

    elif action == 'Update':
        value = command_split[2]
        if matrix[current_position[0]][current_position[1]] != '.':
            matrix[current_position[0]][current_position[1]] = value

    elif action == 'Delete':
        if matrix[current_position[0]][current_position[1]] != '.':
            matrix[current_position[0]][current_position[1]] = '.'

    elif action == 'Read':
        if matrix[current_position[0]][current_position[1]] != '.':
            print(matrix[current_position[0]][current_position[1]])

    command = input()

for row in matrix:
    print(*row, sep=' ')
