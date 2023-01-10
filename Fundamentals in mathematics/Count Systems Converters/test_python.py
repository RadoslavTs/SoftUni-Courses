initial_value = input()
check_list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '.')
hex_digit = initial_value.upper()
check_flag = True
decimal_flag = False
number_of_decimals = 0
explanation_string_one = ""
explanation_string_two = ""
explanation = ""
legend = f"Letter legend: A = 10, B = 11, C = 12, D = 13, E = 14, F = 15 \n"
letter_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

for digit in hex_digit:
    if digit == ".":
        number_of_decimals += 1
        decimal_flag = True
    if number_of_decimals > 1:
        check_flag = False
        break

if check_flag:
    for digit in hex_digit:
        if digit not in check_list:
            check_flag = False
            break

if check_flag and not decimal_flag:
    decimal_result = int()
    for sequence in range(1, len(hex_digit) + 1):
        temp_digit = hex_digit[sequence - 1]
        if temp_digit.isdigit():
            temp_digit = int(temp_digit)
        temp_power = len(hex_digit) - sequence
        temp_multiplier = 16 ** (len(hex_digit) - sequence)
        explanation_string_one += f"({temp_digit} x 16^{temp_power}) + "
        if temp_digit in letter_dict.keys:
            temp_digit = letter_dict[temp_digit]
        temp_number = temp_digit * temp_multiplier
        decimal_result += temp_number
        explanation_string_two += f"{temp_number} + "
    explanation_string_one = explanation_string_one[:-3]
    explanation_string_two = explanation_string_two[:-3]
    explanation = f"Letter legend: A = 10, B = 11, C = 12, D = 13, E = 14, F = 15" '\n' +\
                  f"Hex number: {hex_digit} = {explanation_string_one} = {explanation_string_two}"
    print("explanation", explanation)
    print("result", f"The decimal representation of {hex_digit} is {decimal_result}")

elif check_flag and decimal_flag:
    explanation_string_three = ""
    explanation_string_four = ""
    decimal_result = float()
    hex_digit_float = hex_digit.split(".")
    first_half = hex_digit_float[0]
    second_half = hex_digit_float[1]
    for sequence_two in range(1, len(first_half) + 1):
        temp_digit = first_half[sequence_two - 1]
        if temp_digit.isdigit():
            temp_digit = int(temp_digit)
        temp_power = len(first_half) - sequence_two
        temp_multiplier = 16 ** (len(first_half) - sequence_two)
        explanation_string_one += f"({temp_digit} x 16^{temp_power}) + "
        if temp_digit in letter_dict:
            temp_digit = letter_dict[temp_digit]
        temp_number = temp_digit * temp_multiplier
        decimal_result += temp_number
        explanation_string_two += f"{temp_number} + "
    explanation_string_one = explanation_string_one[:-3]
    explanation_string_two = explanation_string_two[:-3]
    for sequence_three in range(1, len(second_half) + 1):
        temp_digit = second_half[sequence_three - 1]
        if temp_digit.isdigit():
            temp_digit = int(temp_digit)
        temp_power = -sequence_three
        temp_multiplier = 16 ** temp_power
        explanation_string_three += f"({temp_digit} x 16^{temp_power}) + "
        if temp_digit in letter_dict:
            temp_digit = letter_dict[temp_digit]
        temp_number = temp_digit * temp_multiplier
        decimal_result += temp_number
        explanation_string_four += f"{temp_number} + "
    explanation_string_three = explanation_string_three[:-3]
    explanation_string_four = explanation_string_four[:-3]
    explanation_whole = f"Hex number whole: {first_half} = {explanation_string_one} = {explanation_string_two} \n"
    explanation_fraction = f"Hex number fraction: {second_half} = {explanation_string_three} = {explanation_string_four}"
    explanation = f"{legend} {explanation_whole} {explanation_fraction}"
    print("explanation", explanation)
    print("result", f"The decimal representation of {hex_digit} is the sum of the whole and the fraction {decimal_result}")
else:
    print("explanation", "input number is not hexadecimal!")
    print("result", "")