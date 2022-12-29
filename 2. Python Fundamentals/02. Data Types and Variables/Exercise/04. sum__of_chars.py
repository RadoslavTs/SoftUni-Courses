number_of_lines = int(input())
total_sum = 0
for sequence in range(number_of_lines):
    input_character = input()
    total_sum += ord(input_character)
print(f"The sum equals: {total_sum}")