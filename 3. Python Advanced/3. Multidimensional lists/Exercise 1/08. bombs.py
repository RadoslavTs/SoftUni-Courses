matrix_size = int(input())

matrix = []

for row in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

indexes = ((int(x) for x in coordinate.split(",")) for coordinate in input().split())

directions = (
    (-1, 0),  #up
    (1, 0),   #down
    (0, 1),   #right
    (0, -1),  #left
    (-1, 1),  #top-right
    (-1, -1), #top-left
    (1, -1),  #bottom-left
    (1, 1),   #bottom-right
    (0, 0),   #current
)

for row, col in indexes:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y
        if 0 <= r < matrix_size and 0 <= c < matrix_size:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(matrix_size) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for row in matrix:
    print(' '.join(str(x) for x in row))
