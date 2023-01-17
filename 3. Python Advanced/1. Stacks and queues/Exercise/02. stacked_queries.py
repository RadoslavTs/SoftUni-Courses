from collections import deque

numbers = deque()

map_functions = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None,
}

for _ in range(int(input())):
    number_data = [int(x) for x in input().split()]
    map_functions[number_data[0]](number_data)

numbers.reverse()

print(*numbers, sep=", ")


# number_of_lines = int(input())
# my_stack = []
# for sequence in range(number_of_lines):
#     input_command = input()
#     if input_command.startswith("1"):
#         my_stack.append(int(input_command.split()[1]))
#     elif input_command == '2':
#         if my_stack:
#             my_stack.pop()
#     elif input_command == '3' and my_stack:
#         print(max(my_stack))
#     elif input_command == '4' and my_stack:
#         print((min(my_stack)))
# final_output = []
# for element in range(len(my_stack)):
#     final_output.append(str(my_stack.pop()))
# print(', '.join(final_output))