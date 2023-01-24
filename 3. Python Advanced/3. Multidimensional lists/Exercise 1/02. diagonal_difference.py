matrix_size = int(input())
matrix = []

for row in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

diagonal_one_sum = 0
diagonal_two_sum = 0
diagonal_one = []
diagonal_two = []

for i in range(matrix_size):
    diagonal_one_sum += matrix[i][i]
    diagonal_one.append(matrix[i][i])

for j in range(matrix_size):
    diagonal_two_sum += matrix[j][matrix_size-1-j]
    diagonal_two.append(matrix[j][matrix_size-1-j])


print(f"{abs(diagonal_one_sum-diagonal_two_sum)}")
