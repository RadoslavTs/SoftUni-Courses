list_of_numbers = input().split(", ")
count_of_beggars = int(input())
counter_index = 0
resulting_list = []
while counter_index < count_of_beggars:
    sum_for_current_begger = 0
    for sequence in range(counter_index, len(list_of_numbers), count_of_beggars):
        sum_for_current_begger += int(list_of_numbers[sequence])
    counter_index += 1
    resulting_list.append(sum_for_current_begger)
print(resulting_list)