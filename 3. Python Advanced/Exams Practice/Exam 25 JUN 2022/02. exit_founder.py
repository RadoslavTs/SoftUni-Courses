from collections import deque

players_order = deque(input().split(', '))

matrix = []
escape = False
trap = False
player = ''
jerry_wall = False
tom_wall = False

for row in range(6):
    matrix.append(input().split())

while True:
    input_coordinates = input().split(', ')
    row = int(input_coordinates[0][1])
    col = int(input_coordinates[1][0])
    current_player = players_order.popleft()
    players_order.append(current_player)
    if current_player == "Jerry" and jerry_wall == False:
        if matrix[row][col] == 'E':
            escape = True
            player = current_player
            print(f"{player} found the Exit and wins the game!" )
            break

        elif matrix[row][col] == 'T':
            jerry_wall = False
            trap = True
            winner = players_order[0]
            print(f"{current_player} is out of the game! The winner is {winner}." )
            break

        elif matrix[row][col] == 'W':
            jerry_wall = True
            print(f"{current_player} hits a wall and needs to rest.")
            continue

    elif current_player == "Tom" and tom_wall == False:
        if matrix[row][col] == 'E':
            escape = True
            player = current_player
            print(f"{player} found the Exit and wins the game!" )
            jerry_wall = False
            break

        elif matrix[row][col] == 'T':
            jerry_wall = False
            trap = True
            winner = players_order[0]
            print(f"{current_player} is out of the game! The winner is {winner}." )
            break

        elif matrix[row][col] == 'W':
            tom_wall = True
            print(f"{current_player} hits a wall and needs to rest.")
            continue

    else:
        if current_player == "Jerry" and jerry_wall == True:
            jerry_wall = False
        elif current_player == "Tom" and tom_wall == True:
            tom_wall = False

