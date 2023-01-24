from collections import deque

rows, columns = [int(x) for x in input().split()]

snake = deque(list(input()))
matrix = []
current_snake = snake.copy()
current_row = 1
for i in range(rows):
    matrix.append(deque())
    for j in range(columns):
        if current_row % 2 != 0:
            current_character = current_snake.popleft()
            matrix[i].append(current_character)
            current_snake.append(current_character)
        else:
            current_character = current_snake.popleft()
            matrix[i].appendleft(current_character)
            current_snake.append(current_character)
    current_row += 1

for row in matrix:
    print(''.join(row))
