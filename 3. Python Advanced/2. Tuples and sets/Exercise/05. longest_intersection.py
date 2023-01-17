number = int(input())
max_intersection = 0
resulting_intersection = set()
for sequence in range(number):
    first_range, second_range = input().split('-')
    first_range_lower, first_range_higher = first_range.split(',')
    second_range_lower, second_range_higher = second_range.split(',')

    first_range_set = set()
    second_range_set = set()
    for sequence_one in range(int(first_range_lower), int(first_range_higher)+1):
        first_range_set.add(sequence_one)
    for sequence_two in range(int(second_range_lower), int(second_range_higher)+1):
        second_range_set.add(sequence_two)

    resulting_range = first_range_set.intersection(second_range_set)
    if len(resulting_range) > max_intersection:
        max_intersection = len(resulting_range)
        resulting_intersection = resulting_range

range_string = ', '.join(map(lambda x: f"{x}", resulting_intersection))
print(f"Longest intersection is [{range_string}] with length {max_intersection}")

