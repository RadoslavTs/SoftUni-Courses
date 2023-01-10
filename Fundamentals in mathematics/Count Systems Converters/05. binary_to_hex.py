print("Welcome to the binary to hexadecimal converter!\n")
binary_number = input("Please enter binary number: ")
initial_number = binary_number
resulting_number = ""
binary_dict = {"0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6", "0111": "7",
               "1000": "8", "1001": "9", "1010": "A", "1011": "B", "1100": "C", "1101": "D", "1110": "E", "1111": "F"}
print("Convert every 4 binary digits (from bit0) to hex digit (see conversion table below):")
counter = 1
explanation_string_one = ""
explanation_string_two = ""
while binary_number:
    current_number = binary_number[-4:]
    if len(current_number) == 4:
        resulting_number += binary_dict[current_number]
    else:
        if len(current_number) == 3:
            current_number = "0" + current_number
        elif len(current_number) == 2:
            current_number = "00" + current_number
        elif len(current_number) == 1:
            current_number = "000" + current_number
        resulting_number += binary_dict[current_number]
    if explanation_string_one:
        explanation_string_one = current_number + " " + explanation_string_one
        explanation_string_two = binary_dict[current_number] + "    " + explanation_string_two
    else:
        explanation_string_one = current_number
        explanation_string_two = binary_dict[current_number]
    print(f"for digit {counter} ({current_number}) the corresponding hex digit is {binary_dict[current_number]}")
    counter += 1
    binary_number = binary_number[:-4]
resulting_number = resulting_number[::-1]
print(f"Binary digits:         {explanation_string_one}")
print(f"Hexadecimal digits:     {explanation_string_two}\n")
print(f"The hexadecimal representation of {initial_number} is {resulting_number}")