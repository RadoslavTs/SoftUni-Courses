print("Welcome to the binary to decimal converter!\n")
binary_digit = input("Please enter binary number: ")
binary_set = set(binary_digit)
check_set = {'0', '1'}
check_set_float = {'0', '1', '.'}
explanation_string_one = ""
explanation_string_two = ""
if check_set == binary_set or binary_set == {'0'} or binary_set == {'1'}:
    decimal_result = int()
    for sequence in range(1, len(binary_digit) + 1):
        temp_digit = int(binary_digit[sequence - 1])
        temp_power = len(binary_digit) - sequence
        temp_multiplier = 2 ** (len(binary_digit) - sequence)
        temp_number = temp_digit * temp_multiplier
        decimal_result += temp_number
        explanation_string_one += f"({temp_digit} x 2^{temp_power}) + "
        explanation_string_two += f"{temp_number} + "

    # Explanation notes
    explanation_string_one = explanation_string_one[:-3]
    explanation_string_two = explanation_string_two[:-3]
    final_explanation = explanation_string_one + " = " + explanation_string_two
    print("Decimal calculation steps:")
    print(f"Binary number: {binary_digit} = {explanation_string_one} = {explanation_string_two}")
    print(f"The decimal representation of {binary_digit} is {decimal_result}")

    print(final_explanation)
elif check_set_float == binary_set:
    explanation_string_three = ""
    explanation_string_four = ""
    decimal_result = float()
    split_digit = binary_digit.split(".")
    first_half = split_digit[0]
    second_half = split_digit[1]
    temp_number = float()
    for sequence in range(1, len(first_half) + 1):
        temp_digit = int(first_half[sequence - 1])
        temp_power = len(first_half) - sequence
        temp_multiplier = 2 ** (len(first_half) - sequence)
        temp_number = temp_digit * temp_multiplier
        decimal_result += temp_number
        explanation_string_one += f"({temp_digit} x 2^{temp_power}) + "
        explanation_string_two += f"{temp_number} + "
    for sequence_two in range(1, len(second_half) + 1):
        temp_digit = int(second_half[sequence_two-1])
        temp_power = -sequence_two
        temp_multiplier = 2 ** (-sequence_two)
        temp_digit_number = temp_digit * temp_multiplier
        decimal_result += temp_digit_number
        explanation_string_three += f"({temp_digit} x 2^{temp_power}) + "
        explanation_string_four += f"{temp_digit_number} + "
    explanation_string_one = explanation_string_one[:-3]
    explanation_string_two = explanation_string_two[:-3]
    final_explanation = explanation_string_one + " = " + explanation_string_two
    print("Decimal calculation steps:")
    print(f"Binary number: {binary_digit} = {explanation_string_one} + {explanation_string_three} ="
          f" {explanation_string_two} + {explanation_string_four}")
    print(f"The decimal representation of {binary_digit} is {decimal_result}")
else:
    print("input number is not binary")
