def bunny_pos_func(matrice, num):
    for i in range(num):
        for j in range(num):
            if matrice[i][j] == "B":
                return [i, j]


def max_eggs_func(matrice, rol, cow, num):
    best_eggs = 0
    dir_list = []
    direct = ""

    if cow + 1 < num:  # right
        current_sum = 0
        cur_dir_list = []
        for i in range(cow + 1, num):
            if matrice[rol][i].isdigit():
                current_sum += int(matrice[rol][i])
                cur_dir_list.append([rol, i])
            else:
                break
        if current_sum > best_eggs:
            best_eggs = current_sum
            direct = "right"
            dir_list = cur_dir_list

    if cow - 1 >= 0:  # left
        current_sum = 0
        cur_dir_list = []
        for i in range(cow - 1, -1, -1):
            if matrice[rol][i].isdigit():
                current_sum += int(matrice[rol][i])
                cur_dir_list.append([rol, i])
            else:
                break
        if current_sum > best_eggs:
            best_eggs = current_sum
            direct = "left"
            dir_list = cur_dir_list

    if rol + 1 <= num - 1:  # down
        current_sum = 0
        cur_dir_list = []
        for i in range(rol + 1, num):
            if matrice[i][cow].isdigit():
                current_sum += int(matrice[i][cow])
                cur_dir_list.append([i, cow])
            else:
                break
        if current_sum > best_eggs:
            best_eggs = current_sum
            direct = "down"
            dir_list = cur_dir_list

    if rol - 1 >= 0:  # up
        current_sum = 0
        cur_dir_list = []
        for i in range(rol - 1, -1, -1):
            if matrice[i][cow].isdigit():
                current_sum += int(matrice[i][cow])
                cur_dir_list.append([i, cow])
            else:
                break
        if current_sum > best_eggs:
            best_eggs = current_sum
            direct = "up"
            dir_list = cur_dir_list

    return best_eggs, direct, dir_list


n = int(input())
matrix = [[x for x in input().split()] for row in range(n)]

bunny_position = bunny_pos_func(matrix, n)
bunny_row, bunny_col = bunny_position

max_eggs, direction, directions = max_eggs_func(matrix, bunny_row, bunny_col, n)

if max_eggs > 0:
    print(direction)
    for dir in directions:
        print(dir)
    print(max_eggs)
else:
    print(max_eggs)
