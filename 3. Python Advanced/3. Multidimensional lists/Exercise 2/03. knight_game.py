n = int(input())

matrix = [list(input()) for row in range(n)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, -2),
    (1, 2),
)
removed_horses = 0

while True:
    max_attacks = 0
    horse_max_attacks_pos = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                current_attacks = 0
                for pos in positions:
                    if 0 <= row + pos[0] < n and 0 <= col + pos[1] < n:
                        if matrix[row + pos[0]][col + pos[1]] == "K":
                            current_attacks += 1
                if current_attacks > max_attacks:
                    max_attacks = current_attacks
                    horse_max_attacks_pos = [row, col]
    if horse_max_attacks_pos:
        r, c = horse_max_attacks_pos[0], horse_max_attacks_pos[1]
        matrix[r][c] = "0"
        removed_horses += 1
    else:
        break

print(removed_horses)
