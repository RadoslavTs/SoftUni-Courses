count_of_input_lines = int(input())
unique_elements = set()
for sequence in range(count_of_input_lines):
    input_line = input().split()
    for element in input_line:
        unique_elements.add(element)
for result in unique_elements:
    print(result)
