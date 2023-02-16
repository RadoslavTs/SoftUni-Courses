def traversed(where_to, new_rol, new_col):
    posit = []
    if where_to == "up" and new_rol < 0:
        new_rol = len(board) - 1
        santa_moved(new_rol, new_col)
    elif where_to == 'down' and new_rol > len(board)-1:
        new_rol = 0
        santa_moved(new_rol, new_col)
    elif where_to == 'left' and new_col < 0:
        new_col = len(board[0]) - 1
        santa_moved(new_rol, new_col)
    elif where_to == 'right' and new_col > len(board[0]) -1:
        new_col = 0
        santa_moved(new_rol, new_col)

    posit = [new_rol, new_col]
    return posit


def santa_moved(rol, col):
    global decorations
    global cookies
    global gifts
    global total_items
    if board[rol][col] == ".":
        board[rol][col] = 'Y'

    elif board[rol][col] == "D":
        decorations += 1
        total_items -= 1
        board[rol][col] = 'Y'

    elif board[rol][col] == "C":
        cookies += 1
        total_items -= 1
        board[rol][col] = 'Y'

    elif board[rol][col] == "G":
        gifts += 1
        total_items -= 1
        board[rol][col] = 'Y'


def move_command(where_to, how_much, posit):
    for _ in range(how_much):
        new_row, new_col = posit[0] + directions[where_to][0], posit[1] + directions[where_to][1]
        if 0 <= new_row < board_rows and 0 <= new_col < board_columns:
            santa_moved(new_row, new_col)
            posit = [new_row, new_col]
        else:
            posit = traversed(where_to, new_row, new_col)

        if total_items == 0:
            break
        board[posit[0]][posit[1]] = 'x'

    return posit


board_size = list(map(int, input().split(', ')))
board_rows, board_columns = board_size

board = []
santa_position = []
total_items = 0
decorations = 0
gifts = 0
cookies = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for row in range(board_rows):
    string_to_append = input().split()
    board.append(string_to_append)
    if 'Y' in string_to_append:
        santa_position = [row, string_to_append.index('Y')]
    if 'G' in string_to_append:
        total_items += string_to_append.count('G')
    if 'C' in string_to_append:
        total_items += string_to_append.count('C')
    if 'D' in string_to_append:
        total_items += string_to_append.count('D')

board[santa_position[0]][santa_position[1]] = 'x'

command = input()

while command != "End":
    action, steps = [int(x) if x.isdigit() else x for x in command.split('-')]
    santa_position = move_command(action, steps, santa_position)
    if total_items == 0:
        break

    command = input()

if total_items == 0:
    print("Merry Christmas!")

board[santa_position[0]][santa_position[1]] = 'Y'
print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
for row in board:
    print(' '.join(row))
