def print_matrix():
    print_result = ''
    for row in matrix:
        print_result += '[' + ', '.join(str(x) for x in row) + ']''\n'
    return print(print_result)


def user_input(matrix_size, player):
    player_move = int(input(f'Player {player}, please choose a column: '))
    player_move -= 1
    if matrix[0][player_move] != 0:
        return print('No more space in this column'), user_input(matrix_size, player)

    for row in range(matrix_size-1, -1, -1):
        if matrix[row][player_move] == 0:
            if player == 1:
                matrix[row][player_move] = player
            elif player == 2:
                matrix[row][player_move] = player
            print_matrix()
            break
        else:
            continue


def create_matrix(rows, columns):
    matrix = []
    for rol in range(matrix_rows):
        matrix.append([0] * matrix_columns)

    return matrix


def check_win(rows, columns, player, goal):
    player_one_win = False
    player_count_same = 0
    for rol in range(rows-1, -1, -1):
        for col in range(0, columns):
            current_position = [rol, col]
            if matrix[current_position[0]][current_position[1]] == player:
                player_count_same = 1
                for direction in directions.keys():
                    for _ in range(goal):
                        if not player_one_win:
                            if 0 <= current_position[0] + directions[direction][0] < matrix_rows and 0 <= current_position[1] + directions[direction][1] < matrix_columns:
                                new_position = [current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]]
                                if matrix[new_position[0]][new_position[1]] == player:
                                    player_count_same += 1
                                    current_position = [new_position[0], new_position[1]]
                                    if player_count_same == goal:
                                        return True
                                else:
                                    player_count_same = 1
                                    break
                            else:
                                player_count_same = 1
                                break

        #     elif player_one_flag:
        #         break
        #     else:
        #         continue
        # if player_one_win:
        #     break


def check_available_places(playground, columns):
    check_zero = False
    for col in range(columns):
        if playground[0][col] == 0:
            check_zero = True

    if not check_zero:
        return False
    else:
        return True




matrix_columns = 7
matrix_rows = 6

matrix = create_matrix(matrix_rows, matrix_columns)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
    "up_left": [-1, -1],
    "up_right": [-1, 1],
    "down_left": [1, -1],
    "down_right": [1, 1]
}

needed_same = 4
player_one_flag = False
player_two_flag = False

while True:
    if not check_available_places(matrix, matrix_columns):
        break

    user_input(len(matrix), 1)
    player_one_flag = check_win(matrix_rows, matrix_columns, 1, needed_same)
    if player_one_flag:
        break

    user_input(len(matrix), 2)
    player_two_flag = check_win(matrix_rows, matrix_columns, 2, needed_same)
    if player_two_flag:
        break

if player_one_flag:
    print("The winner is player 1")
elif player_two_flag:
    print("The winner is player 2")
else:
    print("No winner this time")
