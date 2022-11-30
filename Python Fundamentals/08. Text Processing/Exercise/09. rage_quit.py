# input_line = input()
# last_index = 0
# resulting_string = ""
# for index in range(len(input_line)):
#     if input_line[index].isdigit():
#         digit_index = index
#         repeating_times = int(input_line[index])
#         text_to_repeat = input_line[last_index:digit_index]
#         resulting_string += text_to_repeat * repeating_times
#         last_index = index+1
# resulting_string = resulting_string.upper()
# resulting_set = set(resulting_string)
# print(f"Unique symbols used: {len(resulting_set)}")
# print(resulting_string)


main_string = input()

current_result, result_show, number = "", "", "",

for index, symbols in enumerate(main_string):
    if not symbols.isdigit():
        current_result += symbols
    elif symbols.isdigit():
        number += symbols
        if index + 1 < len(main_string):
            if main_string[index + 1].isdigit():
                continue
        result_show += int(number) * current_result
        current_result, number = "", ""

result_show = result_show.upper()
print(f"Unique symbols used: {len(set(result_show))}")
print(result_show)