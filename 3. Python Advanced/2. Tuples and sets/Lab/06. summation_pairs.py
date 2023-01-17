list_of_number = list(map(int, input().split()))
looked_number = int(input())
iterations = 0
unique_numbers = set()
for sequence in range (len(list_of_number)):
    for sequence_two in range(sequence+1, len(list_of_number)):
        iterations += 1
        number_one = list_of_number[sequence]
        number_two = list_of_number[sequence_two]
        resulting_number = number_one + number_two
        if resulting_number == looked_number:
            print(f'{list_of_number[sequence]} + {list_of_number[sequence_two]} = {looked_number}')
            string_to_add = f"{list_of_number[sequence]}, {list_of_number[sequence_two]}"
            unique_numbers.add(string_to_add)

print(iterations)

for result in unique_numbers:
    first_result, second_result = result.split(', ')
    print(f'({first_result}, {second_result})')
