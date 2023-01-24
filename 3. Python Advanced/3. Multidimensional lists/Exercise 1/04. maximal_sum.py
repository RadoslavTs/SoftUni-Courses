rows, columns = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = 0
indexes = []
for i in range(rows):
    for j in range(columns):
        if i+2 < rows and j+2 < columns:
            current_sum = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + \
                          matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + \
                          matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
            if max_sum < current_sum:
                max_sum = current_sum
                indexes = [i, j, i+1, j+1, i+2, j+2]
        else:
            continue

print(f"Sum = {max_sum}")
print(f"{matrix[indexes[0]][indexes[1]]} {matrix[indexes[0]][indexes[3]]} {matrix[indexes[0]][indexes[5]]}")
print(f"{matrix[indexes[2]][indexes[1]]} {matrix[indexes[2]][indexes[3]]} {matrix[indexes[2]][indexes[5]]}")
print(f"{matrix[indexes[4]][indexes[1]]} {matrix[indexes[4]][indexes[3]]} {matrix[indexes[4]][indexes[5]]}")

