def check_valid_position(rol, cow):
    if 0 <= rol < len(field) and 0 <= cow < len(field):
        return True
    else:
        return False


def new_position(dir):
    rol, col = rover_position[0] + directions[dir][0], rover_position[1] + directions[dir][1]

    return rol, col


def move_operation(rol, cow):
    global water_found
    global rover_position
    global concrete_found
    global metal_found
    global broken

    if field[rol][cow] == 'R':
        print(f"Rover got broken at ({rol}, {cow})")
        broken = True

    elif field[rol][cow] in ['M', 'C', 'W']:
        current_deposit = field[rol][cow]
        if current_deposit == "W":
            print(f"Water deposit found at ({rol}, {cow})")
            water_found += 1
            rover_position = [rol, cow]
        elif current_deposit == "M":
            print(f"Metal deposit found at ({rol}, {cow})")
            metal_found += 1
            rover_position = [rol, cow]
        elif current_deposit == "C":
            print(f"Concrete deposit found at ({rol}, {cow})")
            concrete_found += 1
            rover_position = [rol, cow]
        field[rol][cow] = '-'
    else:
        rover_position = [rol, cow]


def traverse_field(rol, cow, dir):
    global rover_position
    if dir == "left":
        rover_position = [rol, 5]
    elif dir == 'right':
        rover_position = [rol, 0]
    elif dir == 'up':
        rover_position = [5, cow]
    elif dir == 'down':
        rover_position = [0, cow]


field = []
rover_position = []

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for row in range(6):
    row_input = input().split()
    field.append(row_input)
    if "E" in row_input:
        rover_position = [row, row_input.index("E")]
        field[rover_position[0]][rover_position[1]] = '-'

commands = input().split(', ')

water_found = 0
metal_found = 0
concrete_found = 0
broken = False

for command in commands:
    new_row, new_col = new_position(command)
    if check_valid_position(new_row, new_col):
        move_operation(new_row, new_col)
    else:
        traverse_field(new_row, new_col, command)
        move_operation(rover_position[0], rover_position[1])
    if broken:
        break

if water_found > 0 and metal_found > 0 and concrete_found > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

