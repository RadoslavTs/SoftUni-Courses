rows, columns = [int(x) for x in input().split()]

matrix = []

for i in range(rows):
    column = []
    for j in range(columns):
        element = chr(i+97) + chr(i+j+97) + chr(i+97)
        column.append(element)
    matrix.append(column)
    print(' '.join(column))
