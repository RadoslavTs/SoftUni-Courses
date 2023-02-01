n = int(input())

matrix = []
submarine_position = ()
max_hits = 3
direct_hits = 0
remaining_ships = 3

for sequence in range(n):
    input_line = list(input())
    matrix.append(input_line)
    if "S" in input_line:
        submarine_position = (sequence, matrix[sequence].index("S"))
        matrix[submarine_position[0]][submarine_position[1]] = '-'


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while remaining_ships > 0 and direct_hits < max_hits:
    command = input()
    new_row, new_col = submarine_position[0]+directions[command][0], submarine_position[1]+directions[command][1]

    if matrix[new_row][new_col] == '-':
        submarine_position = (new_row, new_col)
        continue

    elif matrix[new_row][new_col] == '*':
        direct_hits += 1
        matrix[new_row][new_col] = '-'
        submarine_position = (new_row, new_col)
        continue

    elif matrix[new_row][new_col] == 'C':
        remaining_ships -= 1
        matrix[new_row][new_col] = '-'
        submarine_position = (new_row, new_col)

matrix[submarine_position[0]][submarine_position[1]] = 'S'

if direct_hits == 3:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_position[0]}, {submarine_position[1]}]!")
elif remaining_ships == 0:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

for row in matrix:
    print(*row, sep='')
