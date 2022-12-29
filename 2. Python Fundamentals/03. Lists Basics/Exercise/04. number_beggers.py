list_of_numbers = input().split(", ")
beggars = int(input())
resulting_list = []
counter_index = 0
list_of_integers = [int(i) for i in list_of_numbers]
while counter_index < beggars:
    sum_for_current_beggar = 0
    for element in range(counter_index, len(list_of_integers), beggars):
        sum_for_current_beggar += list_of_integers[element]
    counter_index += 1
    resulting_list.append(sum_for_current_beggar)
print(resulting_list)