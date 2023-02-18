from collections import deque


def double_triple(rol, cow, play, double=False, triple=False):
    global player_one_score
    global player_two_score
    up_score = int(board[0][cow])
    down_score = int(board[6][cow])
    left_score = int(board[rol][0])
    right_score = int(board[rol][6])
    summation = up_score + down_score + left_score + right_score
    if double and not triple:
        if play == 1:
            player_one_score -= summation * 2
        else:
            player_two_score -= summation * 2
    elif triple and not double:
        if play == 1:
            player_one_score -= summation * 3
        else:
            player_two_score -= summation * 3


def throw_func(rol, cow, play):
    global player_one_score
    global player_two_score
    if 0 <= rol < len(board) and 0 <= cow < len(board[0]):
        if board[rol][cow].isdigit():
            score = int(board[rol][cow])
            if play == 1:
                player_one_score -= score
            else:
                player_two_score -= score
        elif board[rol][cow] == "D":
            double_triple(rol, cow, play, double=True, triple=False)
        elif board[rol][cow] == "T":
            double_triple(rol, cow, play, double=False, triple=True)


board = []

player_one, player_two = input().split(', ')
bulls_eye_position = []
players = deque([1, 2])

for row in range(7):
    input_line = input().split()
    board.append(input_line)
    if "B" in input_line:
        bulls_eye_position = [row, input_line.index("B")]

player_one_score = 501
player_one_throws = 0
player_two_score = 501
player_two_throws = 0
bullseye = False
winner = ''
winner_throws = 0

while player_one_score > 0 or player_two_score > 0:
    throw = input().split(', ')
    row, col = int(throw[0][1:]), int(throw[1][:-1])
    current_player = players.popleft()
    players.append(current_player)
    if current_player == 1:
        player_one_throws += 1
    else:
        player_two_throws += 1
    if row == bulls_eye_position[0] and col == bulls_eye_position[1]:
        bullseye = True
        if current_player == 1:
            winner = player_one
            winner_throws = player_one_throws
        else:
            winner = player_two
            winner_throws = player_two_throws
        break

    throw_func(row, col, current_player)
    if player_one_score <= 0 and player_two_score > 0:
        winner = player_one
        winner_throws = player_one_throws
        break
    elif player_one_score > 0 and player_two_score <= 0:
        winner = player_two
        winner_throws = player_two_throws
        break

print(f"{winner} won the game with {winner_throws} throws!")