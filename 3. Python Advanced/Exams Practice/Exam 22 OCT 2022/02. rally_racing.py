n = int(input())
tracked_car = input()

matrix = []
finish_coordinates = ()
odometer = 0
car_position = (0, 0)
finish_line_passed = False
tunnel_position = []

for row in range(n):
    matrix.append(input().split())
    if "F" in matrix[row]:
        finish_coordinates = (row, matrix[row].index("F"))
    for _ in range(len(matrix[row])):
        if matrix[row][_] == "T":
            tunnel_position.append((row, _))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

command = input()
while command != "End":
    new_row, new_col = car_position[0] + directions[command][0], car_position[1] + directions[command][1]

    if matrix[new_row][new_col] == ".":
        odometer += 10
        car_position = (new_row, new_col)

    elif matrix[new_row][new_col] == "T":
        tunnel_position.remove((new_row, new_col))
        matrix[new_row][new_col] = "."
        car_position = (tunnel_position[0][0], tunnel_position[0][1])
        matrix[tunnel_position[0][0]][tunnel_position[0][1]] = "."
        odometer += 30

    elif matrix[new_row][new_col] == "F":
        matrix[new_row][new_col] = "C"
        odometer += 10
        car_position = (new_row, new_col)
        finish_line_passed = True
        break

    command = input()

if finish_line_passed:
    print(f"Racing car {tracked_car} finished the stage!")
else:
    matrix[car_position[0]][car_position[1]] = "C"
    print(f"Racing car {tracked_car} DNF.")

print(f"Distance covered {odometer} km." )

for row in matrix:
    print(*row, sep='')
