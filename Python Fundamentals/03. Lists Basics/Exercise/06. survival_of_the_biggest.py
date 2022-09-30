# input_string = input()
# resulting_list = input_string.split(" ")
# resulting_list_integers = []
# cleaning_list = []
# output_string = str()
# for integeration in range(len(resulting_list)):
#     resulting_list_integers.append(int(resulting_list[integeration]))
# resulting_list_integers.sort(reverse=True)
# count_of_numbers_to_remove = int(input())
# for removing in range(count_of_numbers_to_remove):
#   cleaning_list.append(resulting_list_integers.pop())
# for removing_two in range(count_of_numbers_to_remove):
#     resulting_list.remove(str(cleaning_list[removing_two]))
# for finishing_string in range(len(resulting_list)):
#     output_string += str(resulting_list[finishing_string]) + ", "
# output_string = output_string[:-2]
# print(output_string)

list_of_numbers = input().split()
remove_quantity = int(input())
int_list = []
final_string = ""
for element in list_of_numbers:
    int_list.append(int(element))
for sequence in range(remove_quantity):
    min_number = min(int_list)
    int_list.remove(min_number)
for finish in int_list:
    final_string += str(finish) + ", "
final_string = final_string[:-2]
print(final_string)