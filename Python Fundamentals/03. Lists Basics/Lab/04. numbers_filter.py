# number = int(input())
# even_list = []
# odd_list = []
# negative_list = []
# positive_list = []
# for sequence in range(number):
#     current_number = int(input())
#     if current_number >= 0:
#         positive_list.append(current_number)
#     else:
#         negative_list.append(current_number)
#     if current_number % 2 == 0 or current_number == 0:
#         even_list.append(current_number)
#     else:
#         odd_list.append(current_number)
# command = input()
# if command == "even":
#     print(even_list)
# elif command == "odd":
#     print(odd_list)
# elif command == "negative":
#     print(negative_list)
# else:
#     print(positive_list)

number = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

current_number = [int(input()) for sequence in range(number)]
filtered_numbers = []
command = input()
for num in current_number:
    filter_command = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_POSITIVE and num >= 0) or
        (command == COMMAND_NEGATIVE and num < 0)
    )

    if filter_command:
        filtered_numbers.append(num)

print(filtered_numbers)
