rows, columns = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    matrix.append([(x) for x in input().split()])

count_found = 0
indexes = []
for i in range(rows):
    for j in range(columns):
        if i+1 < rows and j+1 < columns:
            if matrix[i][j] == matrix[i][j+1] and matrix[i+1][j] ==matrix[i+1][j+1] and matrix[i][j] == matrix[i+1][j]:
                count_found += 1
        else:
            continue

print(count_found)
