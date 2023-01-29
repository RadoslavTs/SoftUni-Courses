n = int(input())

matrix = []
alice_position = []
tea_bags_collected = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(n):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_position = [row, matrix[row].index("A")]
        matrix[alice_position[0]][alice_position[1]] = "*"

broken_flag = False

while tea_bags_collected < 10:
    command = input()
    rol, col = alice_position[0] + directions[command][0], alice_position[1] + directions[command][1]

    if not (0 <= rol < n and 0 <= col < n):
        break

    alice_position = [rol, col]
    position = matrix[rol][col]
    matrix[rol][col] = "*"

    if position == "R":
        break

    if position.isdigit():
        tea_bags_collected += int(position)

if tea_bags_collected < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*row) for row in matrix]
