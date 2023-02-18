from math import floor


def traverse(rol, cow):
    if rol < 0:
        rol = size - 1
    elif rol > size - 1:
        rol = 0
    elif cow < 0:
        cow = size - 1
    elif cow > size - 1:
        cow = 0

    return rol, cow

size = int(input())
field = []
player_position = []
player_score = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for _ in range(size):
    input_string = input().split()
    field.append(input_string)
    if "P" in input_string:
        player_position = [_, input_string.index("P")]

path = [[player_position[0], player_position[1]]]

command = input()
lost = False

while True:
    new_row, new_col = player_position[0] + directions[command][0], player_position[1] + directions[command][1]
    if not 0 <= new_row < len(field) or not 0 <= new_col < len(field):
        new_row, new_col = traverse(new_row, new_col)
    player_position = [new_row, new_col]
    path.append(player_position)
    if field[new_row][new_col].isdigit():
        player_score += int(field[new_row][new_col])
        field[new_row][new_col] = "P"
    elif field[new_row][new_col] == "X":
        player_score /= 2
        player_score = floor(player_score)
        lost = True
        break

    if player_score >= 100:
        break

    command = input()

if not lost and player_score >= 100:
    print(f"You won! You've collected {player_score} coins.")
else:
    print(f"Game over! You've collected {player_score} coins.")
print("Your path:")
print(*path, sep='\n')