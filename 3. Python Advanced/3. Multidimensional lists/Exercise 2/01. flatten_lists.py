input_list = [[x for x in rows.split()] for rows in input().split("|")]
input_list = input_list[::-1]

for row in input_list:
    print(*row, sep = " ", end=' ')
