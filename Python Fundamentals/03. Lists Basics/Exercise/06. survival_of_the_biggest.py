input_string = input()
resulting_list = input_string.split(" ")
resulting_list_integers = []
cleaning_list = []
output_string = str()
for integeration in range(len(resulting_list)):
    resulting_list_integers.append(int(resulting_list[integeration]))
resulting_list_integers.sort(reverse=True)
count_of_numbers_to_remove = int(input())
for removing in range(count_of_numbers_to_remove):
  cleaning_list.append(resulting_list_integers.pop())
for removing_two in range(count_of_numbers_to_remove):
    resulting_list.remove(str(cleaning_list[removing_two]))
for finishing_string in range(len(resulting_list)):
    output_string += str(resulting_list[finishing_string]) + ", "
output_string = output_string[:-2]
print(output_string)
