print("Welcome to the hexadecimal to binary converter!\n")
check_list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
hex_number = input("Please enter hex number: ")
hex_number = hex_number.upper()
check_flag = True
for digit in hex_number:
    if digit not in check_list:
        check_flag = False
        break

hex_dict = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
            "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
resulting_binary = ""
if check_flag:
    print("Convert each hex digit to 4 binary digits according to the conversion table below:")
    print(hex_dict)
    for sequence in range(0, len(hex_number)):
        resulting_binary += hex_dict[hex_number[sequence]]
        print(f"Digit {hex_number[sequence]} = {hex_dict[hex_number[sequence]]}")
    print(f"The binary representation of {hex_number} = {resulting_binary}")
else:
    print("input number is not decimal!")

