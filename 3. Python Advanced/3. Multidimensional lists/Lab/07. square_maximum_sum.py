rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

max_sum = 0
indexes = []
for i in range(rows):
    for j in range(columns):
        if i+1 < rows and j+1 < columns:
            current_sum = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
            if max_sum < current_sum:
                max_sum = current_sum
                indexes = [i, j, i+1, j+1]
        else:
            continue
print(f"{matrix[indexes[0]][indexes[1]]} {matrix[indexes[0]][indexes[3]]}")
print(f"{matrix[indexes[2]][indexes[1]]} {matrix[indexes[2]][indexes[3]]}")
print(max_sum)
