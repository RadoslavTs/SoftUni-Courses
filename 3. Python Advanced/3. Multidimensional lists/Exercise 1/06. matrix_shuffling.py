rows, columns = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    matrix.append([x for x in input().split()])

command = input().split()
invalid_flag = False
while command[0] != "END":
    if command[0] == "swap" and command[1].isdigit() and command[2].isdigit() and command[3].isdigit() and command[4].isdigit():
        if len(command) != 5 or int(command[1]) >= rows or int(command[2]) >= columns or int(command[3]) >= rows or int(command[4]) > columns:
            print("Invalid input!")
            command = input().split()
            continue
        else:
            row1 = int(command[1])
            col1 = int(command[2])
            row2 = int(command[3])
            col2 = int(command[4])
            number_one = matrix[row1][col1]
            number_two = matrix[row2][col2]
            matrix[row1][col1] = number_two
            matrix[row2][col2] = number_one
            for row in matrix:
                print(' '.join(str(x) for x in row))
    else:
        print("Invalid input!")
        command = input().split()
        continue
    command = input().split()
