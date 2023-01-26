input_list = [[int(x) for x in rows.split()] for rows in input().split("|")]
input_list = input_list[::-1]
resulting_list = []

for row in input_list:
    for item in row:
        resulting_list.append(item)

print(*resulting_list, sep=' ')
