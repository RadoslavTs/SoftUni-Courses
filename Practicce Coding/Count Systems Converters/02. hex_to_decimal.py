print("Welcome to the hexadecimal to decimal converter!\n")
hex_digit = input("Please enter hex number: ")
hex_digit = hex_digit.upper()
decimal_result = int()
explanation_string_one = ""
explanation_string_two = ""
for sequence in range(1, len(hex_digit) + 1):
    temp_digit = hex_digit[sequence - 1]
    if temp_digit.isdigit():
        temp_digit = int(temp_digit)
    temp_power = len(hex_digit) - sequence
    temp_multiplier = 16 ** (len(hex_digit) - sequence)
    explanation_string_one += f"({temp_digit} x 16^{temp_power}) + "
    if temp_digit == "A":
        temp_digit = 10
    elif temp_digit == "B":
        temp_digit = 11
    elif temp_digit == "C":
        temp_digit = 12
    elif temp_digit == "D":
        temp_digit = 13
    elif temp_digit == "E":
        temp_digit = 14
    elif temp_digit == "F":
        temp_digit = 15
    temp_number = temp_digit * temp_multiplier
    decimal_result += temp_number
    explanation_string_two += f"{temp_number} + "


# Explanation notes
explanation_string_one = explanation_string_one[:-3]
explanation_string_two = explanation_string_two[:-3]
print("Letter legend:")
print("A = 10, B = 11, C = 12, D = 13, E = 14, F = 15")
print(f"Hex number: {hex_digit} = {explanation_string_one} = {explanation_string_two}")
print(f"The decimal representation of {hex_digit} is {decimal_result}")