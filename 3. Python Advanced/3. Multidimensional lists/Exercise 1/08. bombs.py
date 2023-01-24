matrix_size = int(input())

matrix = []

for row in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

indexes = input().split()

for bomb in indexes:
    bomb_split = bomb.split(",")
    curr_row = int(bomb_split[0])
    curr_col = int(bomb_split[1])
    if matrix[curr_row][curr_col] > 0:
        bomb_power = matrix[curr_row][curr_col]
        matrix[curr_row][curr_col] = 0
        if curr_row-1 >= 0:
            matrix[curr_row-1][curr_col] -= bomb_power
        if curr_row+1 <= matrix_size:
            matrix[curr_row+1][curr_col] -= bomb_power
        if curr_col-1 >= 0:
            matrix[curr_row][curr_col-1] -= bomb_power
        if curr_col+1 <= matrix_size:
            matrix[curr_row][curr_col+1] -= bomb_power


        for i in range(curr_row+1, matrix_size):
            for j in range(curr_col+1, matrix_size):
                matrix[i][j] -= bomb_power
                if j == matrix_size-1:
                    break

            for j in range(curr_col-1, -1, -1):
                matrix[i][j] -= bomb_power

        for i in range(curr_row-1, -1, -1):
            for j in range(curr_col-1, -1, -1):
                matrix[i][j] -= bomb_power

            for j in range(curr_col+1, matrix_size):
                matrix[i][j] -= bomb_power

alive_cells = 0
total_sum = 0
for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            total_sum += el

print(alive_cells)
print(total_sum)

