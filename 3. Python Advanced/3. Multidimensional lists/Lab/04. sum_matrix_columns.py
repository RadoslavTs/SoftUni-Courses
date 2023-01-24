rows, columns = [int(x) for x in input().split(', ')]
matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split()])

sum_result = 0

for row in range(columns):
    for column in matrix:
        sum_result += column[row]
    print(sum_result)
    sum_result = 0
