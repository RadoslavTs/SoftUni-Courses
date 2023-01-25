def valid_command(comm, row, cow, a, b, size):
    valid_commands = ["left", "right", "up", "down"]
    valid_check = True
    if comm not in valid_commands:
        valid_check = False
    if comm == "left" and cow + b < 0:
        valid_check = False
    if comm == "right" and cow + b > size-1:
        valid_check = False
    if comm == "up" and row + a < 0:
        valid_check = False
    if comm == "down" and row + a > size-1:
        valid_check = False
    if valid_check:
        return True
    else:
        return False


def coal_flag(matrice):
    coal_flag = True
    for row in matrice:
        for el in row:
            if el == "c":
                coal_flag = False
                break
    if coal_flag:
        return True
    else:
        return False


n = int(input())

commands = input().split()

matrix = [[x for x in input().split()] for _ in range(n)]

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

collected_flag = False
coal_collected = 0
move_made_flag = False
end_game_flag = False
for command in commands:
    move_made_flag = False
    if coal_flag(matrix):
        collected_flag = True
        break
    else:
        x, y = directions[command]
        for rol in range(n):
            for col in range(n):
                current_symbol = matrix[rol][col]
                if current_symbol == "s":
                    new_rol, new_col = rol + x, col + y
                    if valid_command(command, rol, col, x, y, n):
                        if matrix[new_rol][new_col] == "*":
                            matrix[new_rol][new_col] = "s"
                            matrix[rol][col] = "*"
                            move_made_flag = True
                            break
                        elif matrix[new_rol][new_col] == "e":
                            matrix[new_rol][new_col] = "s"
                            matrix[rol][col] = "*"
                            end_game_flag = True
                            break
                        elif matrix[new_rol][new_col] == "c":
                            matrix[new_rol][new_col] = "s"
                            matrix[rol][col] = "*"
                            coal_collected += 1
                            move_made_flag = True
                            break
                    else:
                        continue
            if move_made_flag or end_game_flag:
                break
        if end_game_flag:
            break
        if move_made_flag:
            continue

final_position = ''
remaining_coal = 0
if coal_flag(matrix):
    collected_flag = True
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 's':
            final_position = f'({i}, {j})'
        elif matrix[i][j] == "c":
            remaining_coal += 1


if end_game_flag:
    print(f"Game over! {final_position}")
elif collected_flag:
    print(f"You collected all coal! {final_position}")
else:
    print(f"{remaining_coal} pieces of coal left. {final_position}")
