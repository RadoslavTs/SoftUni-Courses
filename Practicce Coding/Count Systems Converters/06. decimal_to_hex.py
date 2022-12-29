print("Welcome to the decimal to hexadecimal converter!\n")
decimal_number = int(input("Please enter decimal number: "))
initial_decimal_number = decimal_number
resulting_number = ""
explanation = ""
bit_position = 0

print("Divide by the base 16 to get the digits from the remainders:\n")
while decimal_number > 0:
    decimal_to_work_with = decimal_number
    remainder = decimal_number % 16
    if remainder == 10:
        remainder = "A"
    elif remainder == 11:
        remainder = "B"
    elif remainder == 12:
        remainder = "C"
    elif remainder == 13:
        remainder = "D"
    elif remainder == 14:
        remainder = "E"
    elif remainder == 15:
        remainder = "F"
    decimal_number = decimal_number // 16
    resulting_number += str(remainder)
    explanation += f"{decimal_to_work_with}/16 with a reminder of {remainder} and digit position {bit_position}\n"
    bit_position += 1

result = resulting_number
resulting_number = resulting_number[::-1]

print(explanation)
print(f"Resulting number {result} should be counted backwards and we get the final result: {resulting_number}")
print(f"The hexadecimal representation of {initial_decimal_number} is {resulting_number}")