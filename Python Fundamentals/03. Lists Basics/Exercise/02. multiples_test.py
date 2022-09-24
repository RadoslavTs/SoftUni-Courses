factor_number = int(input())
count_number = int(input())
resulting_list = []
current_number = 0
for sequence in range(1, count_number + 1):
    resulting_list.append(current_number + factor_number)
    current_number += factor_number
print(resulting_list)