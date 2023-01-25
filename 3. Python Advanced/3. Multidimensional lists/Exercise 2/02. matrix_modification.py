def calc_func(matrice, rol, cow, val, comm):
    if comm == "Add":
        matrice[rol][cow] += val
    elif comm == "Subtract":
        matrice[rol][cow] -= val
        return matrice
    return matrice


def validation_func(rol, cow, size):
    if 0 <= rol <= size-1 and 0 <= cow <= size-1:
        return True
    else:
        return False


n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    input_data = input().split()

    command = input_data[0]

    if command == "END":
        break

    row = int(input_data[1])
    col = int(input_data[2])
    value = int(input_data[3])

    if validation_func(row, col, n,):
        calc_func(matrix, row, col, value, command)

    else:
        print("Invalid coordinates")
        continue

for row in matrix:
    print(' '.join(str(x) for x in row))
