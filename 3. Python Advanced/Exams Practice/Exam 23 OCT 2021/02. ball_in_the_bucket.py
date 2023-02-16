board = []

for row in range(6):
    string = [int(x) if x.isdigit() else x for x in input().split()]
    board.append(string)

score = 0

for throw in range(3):
    input_line = input().split(', ')
    row = int(input_line[0][1:])
    col = int(input_line[1][:-1])
    if 0 <= row < 6 and 0 <= col < 6:
        if board[row][col] == "B":
            board[row][col] = 0
            for _ in range(6):
                score += board[_][col]

prize = ''
if score >= 100:
    if score <= 199:
        prize = "Football"
    elif score <= 299:
        prize = "Teddy Bear"
    else:
        prize = "Lego Construction Set"
    print(f"Good job! You scored {score} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
