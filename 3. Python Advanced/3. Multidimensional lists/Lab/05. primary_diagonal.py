rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

sum_result = 0
index = 0
for row in matrix:
    sum_result += row[index]
    index += 1

print(sum_result)
