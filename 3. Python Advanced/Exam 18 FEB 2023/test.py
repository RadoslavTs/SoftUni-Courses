n = 3
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append([] * i)
        matrix[i][j] = 1

print(matrix)