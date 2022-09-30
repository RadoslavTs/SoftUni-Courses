people_list = input().split()
permutation_number = int(input())
temporary_people_list = []
resulting_list = []
breaking_point = False
while not breaking_point:
    for sequence in range(permutation_number - 1, len(people_list) + 1, permutation_number):
        if sequence < len(people_list):
            resulting_list.append(people_list[sequence])
        if sequence < len(people_list):
            continue
    left_over = len(people_list) - sequence
    del people_list[permutation_number]
print(people_list)
