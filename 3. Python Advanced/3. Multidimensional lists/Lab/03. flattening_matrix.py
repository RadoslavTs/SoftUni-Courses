rows = int(input())
matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

flattened_matrix = []
for row in matrix:
    for col in row:
        flattened_matrix.append(col)

print(flattened_matrix)
