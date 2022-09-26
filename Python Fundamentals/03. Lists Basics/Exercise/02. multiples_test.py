factor_number = int(input())
count_number = int(input())
resulting_list = []
current_number = 0
for sequence in range(1, count_number + 1):
    resulting_list.append(factor_number * sequence)
print(resulting_list)