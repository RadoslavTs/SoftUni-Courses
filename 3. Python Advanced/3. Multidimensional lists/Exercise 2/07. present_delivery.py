def valid_command(comm, row, cow, a, b, size):
    valid_commands = ["left", "right", "up", "down"]
    valid_check = True
    if comm not in valid_commands:
        valid_check = False
    if comm == "left" and b < 0:
        valid_check = False
    if comm == "right" and b > size:
        valid_check = False
    if comm == "up" and a < 0:
        valid_check = False
    if comm == "down" and a > size:
        valid_check = False
    if valid_check:
        return True
    else:
        return False


def current_position(matrice, num):
    for i in range(num):
        for j in range(num):
            if matrice[i][j] == "S":
                return [i, j]




m = int(input())
n = int(input())

matrix = [[x for x in input().split()] for _ in range(n)]

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

command = input()
no_more_presents_flag = False
good_kids_with_presents = 0
bad_kids_with_presents = 0

while command != "Christmas morning":
    if m == 0:
        no_more_presents_flag = True
        command = input()
        break
    current_pos_row, current_pos_col = current_position(matrix, n)
    new_position_row, new_position_col = current_pos_row + directions[command][0], current_pos_col + directions[command][1]
    new_position_value = matrix[new_position_row][new_position_col]
    if not valid_command(command, current_pos_row, current_pos_col, new_position_row, new_position_col, n):
        command = input()
        continue
    if new_position_value == "-" or new_position_value == "X":
        matrix[current_pos_row][current_pos_col] = '-'
        matrix[new_position_row][new_position_col] = 'S'
        command = input()
        continue
    elif new_position_value == "V":
        good_kids_with_presents += 1
        m -= 1
        matrix[current_pos_row][current_pos_col] = '-'
        matrix[new_position_row][new_position_col] = 'S'
        if m == 0:
            no_more_presents_flag = True
            break
        command = input()
        continue
    elif new_position_value == "C":
        matrix[new_position_row][new_position_col] = "S"
        matrix[current_pos_row][current_pos_col] = "-"
        if matrix[new_position_row-1][new_position_col] == "V":
            matrix[new_position_row-1][new_position_col] = "-"
            if m > 0:
                good_kids_with_presents += 1
                m -= 1
        elif matrix[new_position_row-1][new_position_col] == "X":
            matrix[new_position_row - 1][new_position_col] = "-"
            if m > 0:
                bad_kids_with_presents += 1
                m -= 1
        if matrix[new_position_row+1][new_position_col] == "V":
            matrix[new_position_row-1][new_position_col] = "-"
            if m > 0:
                good_kids_with_presents += 1
                m -= 1
        elif matrix[new_position_row+1][new_position_col] == "X":
            matrix[new_position_row - 1][new_position_col] = "-"
            if m > 0:
                bad_kids_with_presents += 1
                m -= 1
        if matrix[new_position_row][new_position_col-1] == "V":
            matrix[new_position_row][new_position_col-1] = "-"
            if m > 0:
                good_kids_with_presents += 1
                m -= 1
        elif matrix[new_position_row][new_position_col-1] == "X":
            matrix[new_position_row][new_position_col-1] = "-"
            if m > 0:
                bad_kids_with_presents += 1
                m -= 1
        if matrix[new_position_row][new_position_col+1] == "V":
            matrix[new_position_row][new_position_col+1] = "-"
            if m > 0:
                good_kids_with_presents += 1
                m -= 1
        elif matrix[new_position_row][new_position_col+1] == "X":
            matrix[new_position_row][new_position_col+1] = "-"
            if m > 0:
                bad_kids_with_presents += 1
                m -= 1
        if m > 0:
            command = input()
        else:
            no_more_presents_flag = True
            break
        continue
    command = input()

good_kids_left = 0

for row in matrix:
    for el in row:
        if el == "V":
            good_kids_left += 1

if m == 0 and good_kids_left > 0:
    print("Santa ran out of presents!")
for row in matrix:
    print(' '.join(row))
if good_kids_left == 0:
    print(f"Good job, Santa! {good_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {good_kids_left} nice kid/s.")
