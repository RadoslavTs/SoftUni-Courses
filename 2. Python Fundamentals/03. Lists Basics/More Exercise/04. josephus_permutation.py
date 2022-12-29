people_list = input().split()
permutation_number = int(input())
temporary_people_list = []
resulting_list = []
resulting_string = ""
current_index = permutation_number
for sequence in range(0, len(people_list)):
    while current_index > len(people_list):
        current_index -= len(people_list)
    resulting_list.append(people_list[current_index-1])
    current_index += permutation_number -1
    del people_list[current_index - permutation_number]
for element in resulting_list:
    resulting_string += element + ","
print(f"[{resulting_string[:-1]}]")