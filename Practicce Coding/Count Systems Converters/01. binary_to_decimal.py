print("Welcome to the binary to decimal converter!\n")
binary_digit = input("Please enter binary number: ")
decimal_result = int()
explanation_string_one = ""
explanation_string_two = ""
for sequence in range(1, len(binary_digit)+1):
    temp_digit = int(binary_digit[sequence-1])
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