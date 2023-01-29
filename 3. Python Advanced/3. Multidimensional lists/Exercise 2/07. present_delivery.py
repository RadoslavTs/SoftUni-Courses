m = int(input())
n = int(input())
matrix = []
santa_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

total_nice_kids = 0
nice_kids_with_presents = 0

for row in range(n):
    matrix.append(input().split())
    if "S" in matrix[row]:
        santa_position = [row, matrix[row].index("S")]
    if "V" in matrix[row]:
        total_nice_kids += matrix[row].count("V")

command = input()

while command != "Christmas morning" and m > 0:
    row, col = directions[command]
    new_row, new_col = santa_position[0] + row, santa_position[1] + col

    if not (0 <= new_row < n and 0 <= new_col < n):
        break

    if matrix[new_row][new_col] == '-':
        matrix[santa_position[0]][santa_position[1]] = '-'
        matrix[new_row][new_col] = "S"
        santa_position = [new_row, new_col]

    elif matrix[new_row][new_col] == 'V':
        if m > 0:
            matrix[new_row][new_col] = "S"
            m -= 1
            nice_kids_with_presents += 1
        else:
            break
        matrix[santa_position[0]][santa_position[1]] = "-"
        santa_position = [new_row, new_col]

    elif matrix[new_row][new_col] == 'X':
        matrix[new_row][new_col] = "S"
        matrix[santa_position[0]][santa_position[1]] = "-"
        santa_position = [new_row, new_col]

    elif matrix[new_row][new_col] == 'C':
        matrix[santa_position[0]][santa_position[1]] = "-"
        santa_position = [new_row, new_col]
        matrix[new_row][new_col] = "S"

        for coord in directions.values():
            if matrix[santa_position[0] + coord[0]][santa_position[1] + coord[1]] == "-":
                continue
            elif matrix[santa_position[0] + coord[0]][santa_position[1] + coord[1]] == "X":
                if m > 0:
                    m -= 1
                    matrix[santa_position[0] + coord[0]][santa_position[1] + coord[1]] = "-"
                    if m == 0:
                        break
                else:
                    break
            elif matrix[santa_position[0] + coord[0]][santa_position[1] + coord[1]] == "V":
                if m > 0:
                    m -= 1
                    nice_kids_with_presents += 1
                    matrix[santa_position[0] + coord[0]][santa_position[1] + coord[1]] = "-"
                    if m == 0:
                        break
                else:
                    break
    if m == 0:
        break
    command = input()

if total_nice_kids - nice_kids_with_presents > 0 and m == 0:
    print("Santa ran out of presents!")
for row in matrix:
    print(*row)
if total_nice_kids == nice_kids_with_presents:
    print(f"Good job, Santa! {nice_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_with_presents} nice kid/s.")
