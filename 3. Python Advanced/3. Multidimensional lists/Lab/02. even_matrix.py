rows = int(input())
matrix = []


for row in range(rows):
    matrix.append([int(x) for x in input().split(', ') if int(x) % 2 == 0])

# for row in matrix:
#     for el in row.copy():
#         if el % 2 != 0:
#             row.remove(el)

print(matrix)
