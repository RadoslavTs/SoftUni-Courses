number = int(input())
matrix = []
searched_flag = False
current_row = 0
current_column = 0

for row in range(number):
    matrix.append([x for x in list(input())])

searched_symbol = input()

for row in matrix:
    for symbol in row:
        if symbol == searched_symbol:
            searched_flag = True
            break
        current_column += 1
        if current_column > 2:
            current_column = 0
    if searched_flag:
        break
    current_row += 1
if searched_flag:
    print(f'({current_row}, {current_column})')
else:
    print(f"{searched_symbol} does not occur in the matrix")
