n, m = list(map(int, input().split()))

playground = []
player_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

moves_made = 0
players_touched = 0
total_players = 3

for row in range(n):
    playground.append(input().split())
    if "B" in playground[row]:
        player_position = [row, playground[row].index("B")]

playground[player_position[0]][player_position[1]] = '-'

command = input()

while command != "Finish":
    new_row, new_col = player_position[0] + directions[command][0], player_position[1] + directions[command][1]
    if 0 <= new_row < len(playground) and 0 <= new_col < len(playground[0]) and players_touched < total_players:
        move_position = playground[new_row][new_col]
        if playground[new_row][new_col] != "O":
            player_position = [new_row, new_col]
            playground[new_row][new_col] = '-'

        if move_position == "P":
            players_touched += 1
            moves_made += 1

        elif move_position == '-':
            moves_made += 1

    command = input()

print("Game over!")
print(f"Touched opponents: {players_touched} Moves made: {moves_made}")