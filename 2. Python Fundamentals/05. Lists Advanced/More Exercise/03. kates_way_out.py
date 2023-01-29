# rows = int(input())
#
# matrix = []
# moves_out = 0
# kate_position = []
#
# for row in range(rows):
#     matrix.append(list(input()))
#
#     if "k" in matrix[row]:
#         kate_position = [row, matrix[row].index("k")]
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1)
# }
#
# length = len(matrix[0])
#
# kate_out_flag = False
# stuck_flag = False
#
# while True:
#
#     for direction in directions.values():
#         new_rol, new_col = kate_position[0] + direction[0], kate_position[1] + direction[1]
#         if 0 <= new_rol < rows and 0 <= new_col < length:
#             if matrix[new_rol][new_col] == " ":
#                 kate_position = [new_rol, new_col]
#                 matrix[new_rol][new_col] = "k"
#                 moves_out += 1
#                 break
#             elif matrix[new_rol][new_col] == "#":
#                 continue
#             else:
#                 continue
#
#         else:
#             moves_out += 1
#             kate_out_flag = True
#             continue
#
#     current_situation = []
#     on_left = [kate_position[0], kate_position[1] -1]
#     on_right = [kate_position[0], kate_position[1] + 1]
#     on_up = [kate_position[0] - 1, kate_position[1]]
#     on_down = [kate_position[0] + 1, kate_position[1]]
#
#     if 0 <= on_left[0] < rows and 0 <= on_left[1] < length:
#         current_situation.extend(matrix[on_left[0]][on_left[1]])
#     if 0 <= on_right[0] < rows and 0 <= on_right[1] < length:
#         current_situation.extend(matrix[on_right[0]][on_right[1]])
#     if 0 <= on_up[0] < rows and 0 <= on_up[1] < length:
#         current_situation.extend(matrix[on_up[0]][on_up[1]])
#     if 0 <= on_down[0] < rows and 0 <= on_down[1] < length:
#         current_situation.extend(matrix[on_down[0]][on_down[1]])
#
#     if "k" in current_situation and current_situation.count("#") == 3:
#         stuck_flag = True
#         break
#
#     if kate_out_flag:
#         break
#
# if kate_out_flag:
#     print(f"Kate got out in {moves_out} moves")
# if stuck_flag:
#     print("Kate cannot get out")

def find_way_out(r, c, moves):
    if not (0 <= r < len(matrix) and 0 <= c < len(matrix[0])):
        return moves

    if matrix[r][c] == "#":
        return 0

    matrix[r][c] = "#"

    result1 = find_way_out(r + 1, c, moves + 1)
    result2 = find_way_out(r - 1, c, moves + 1)
    result3 = find_way_out(r, c + 1, moves + 1)
    result4 = find_way_out(r, c - 1, moves + 1)

    return max(result1, result2, result3, result4)


matrix = []
kate_pos = []

for row in range(int(input())):
    matrix.append(list(input()))

    if "k" in matrix[row]:
        kate_pos = [row, matrix[row].index("k")]

out_in = find_way_out(kate_pos[0], kate_pos[1], 0)

if not out_in:
    print(f"Kate cannot get out")
else:
    print(f"Kate got out in {out_in} moves")