def escape_check(comm, rol, cow, a, b, size):
    valid_check = False
    if comm == "L" and b < 0:
        valid_check = True
    if comm == "R" and b > size-1:
        valid_check = True
    if comm == "U" and a < 0:
        valid_check = True
    if comm == "D" and a > size-1:
        valid_check = True
    if valid_check:
        return True
    else:
        return False


def current_position(matrice, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if matrice[i][j] == "P":
                return [i, j]


def bunny_pos(matrice, rows, columns):
    bunny_positions = []
    for i in range(rows):
        for j in range(columns):
            if matrice[i][j] == "B":
                bunny_positions.append((i, j))
    return bunny_positions


def bunny_spread(positions, rol, cow):
    for pos in positions:
        bunny_row, bunny_col = pos[0], pos[1]
        if bunny_col - 1 >= 0:
            matrix[bunny_row][bunny_col-1] = "B"
        if bunny_col + 1 < cow:
            matrix[bunny_row][bunny_col+1] = "B"
        if bunny_row - 1 >= 0:
            matrix[bunny_row-1][bunny_col] = "B"
        if bunny_row + 1 < rol:
            matrix[bunny_row+1][bunny_col] = "B"


def bunny_lapped(matrice):
    list_to_check = []
    for rol in matrice:
        for el in rol:
            list_to_check.append(el)
    if "P" not in list_to_check:
        return True
    else:
        return False


n, m = (int(x) for x in input().split())

matrix = [[x for x in list(input())] for _ in range(n)]

commands = list(input())

directions = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

player_escaped = False
escape_coordinates = []
last_coordinates = []

for command in commands:
    player_row, player_col = current_position(matrix, n, m)
    bunny_positions = bunny_pos(matrix, n, m)

    x, y = directions[command]

    new_player_row, new_player_col = player_row + x, player_col + y

    if escape_check(command, player_row, player_col, new_player_row, new_player_col, n):
        player_escaped = True
        escape_coordinates = [player_row, player_col]
        matrix[player_row][player_col] = "."
        bunny_spread(bunny_positions, n, m)
        break
    else:
        if matrix[new_player_row][new_player_col] == ".":
            matrix[new_player_row][new_player_col] = "P"
            matrix[player_row][player_col] = "."
            bunny_spread(bunny_positions, n, m)
            if bunny_lapped(matrix):
                last_coordinates = [new_player_row, new_player_col]
                break
        else:
            bunny_spread(bunny_positions, n, m)
            if bunny_lapped(matrix):
                last_coordinates = [new_player_row, new_player_col]
                break

if player_escaped:
    for row in matrix:
        print(''.join(row))

    print(f"won: {' '.join(str(x) for x in escape_coordinates)}")
elif bunny_lapped:
    for row in matrix:
        print(''.join(row))
    print(f"dead: {' '.join(str(x) for x in last_coordinates)}")
#
# rows, cols = [int(x) for x in input().split()]
# matrix = [[x for x in input()] for _ in range(rows)]
# commands = input()
#
# winner, movement = False, {
#     "U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]
# }
#
#
# def find_player_position():
#     for row in range(rows):
#         if "P" in matrix[row]:
#             return row, matrix[row].index("P")
#
#
# def player_alive(row, col):
#     if matrix[row][col] == "B":
#         show_result("dead")
#
#
# def check_valid_index(row, col, player=False):
#     global winner
#     if 0 <= row < rows and 0 <= col < cols:
#         return True
#     if player:
#         winner = True
#
#
# def bunnies_position():
#     position = []
#     for row in range(rows):
#         for col in range(cols):
#             if matrix[row][col] == "B":
#                 position.append(row)
#                 position.append(col)
#     return position
#
#
# def bunnies_moves(bunnies_pos):
#     for i in range(0, len(bunnies_pos), 2):
#         row, col = bunnies_pos[i], bunnies_pos[i + 1]
#         for bunnie_move in movement:
#             new_row, new_col = row + movement[bunnie_move][0], col + movement[bunnie_move][1]
#             if check_valid_index(new_row, new_col):
#                 matrix[new_row][new_col] = "B"
#
#
# def show_result(status="won"):
#     [print(*matrix[row], sep="") for row in range(rows)]
#     print(f"{status}: {player_row} {player_col}")
#     exit()
#
#
# player_row, player_col = find_player_position()
# matrix[player_row][player_col] = "."
# for command in commands:
#     player_movement_row, player_movement_col = player_row + movement[command][0], player_col + movement[command][1]
#     if check_valid_index(player_movement_row, player_movement_col, True):
#         player_row, player_col = player_movement_row, player_movement_col
#     bunnies_moves(bunnies_position())
#     if winner:
#         show_result()
#     if check_valid_index(player_movement_row, player_movement_col):
#         player_alive(player_movement_row, player_movement_col)