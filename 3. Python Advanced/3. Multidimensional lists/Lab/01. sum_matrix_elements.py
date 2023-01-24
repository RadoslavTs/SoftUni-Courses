rows, columns = map(int, input().split(', '))
matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
total = 0
for lst in matrix:
    for element in lst:
        total += element
print(total)
print(matrix)