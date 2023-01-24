matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]

diagonal_one_sum = 0
diagonal_two_sum = 0
diagonal_one = []
diagonal_two = []

primary = [matrix[r][r] for r in range(len(matrix))]
secondary = [matrix[r][len(matrix)-1-r] for r in range(len(matrix))]
print(primary)
print(secondary)

# for j in range(len(matrix)):
#     diagonal_two_sum += matrix[j][len(matrix)-1-j]
#     diagonal_two.append(matrix[j][len(matrix)-1-j])
#
# print(f"Primary diagonal: {', '.join(str(x) for x in diagonal_one)}. Sum: {diagonal_one_sum}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in diagonal_two)}. Sum: {diagonal_two_sum}")
