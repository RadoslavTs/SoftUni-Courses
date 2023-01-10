print("Welcome to the decimal to binary converter!\n")
decimal_number = int(input("Please enter decimal number: "))
initial_decimal_number = decimal_number
resulting_number = ""
explanation = ""
bit_position = 0

print("Divide by the base 2 to get the digits from the remainders:\n")
while initial_decimal_number > 0:
    decimal_to_work_with = initial_decimal_number
    remainder = initial_decimal_number % 2
    initial_decimal_number = initial_decimal_number // 2
    resulting_number += str(remainder)
    explanation += f"{decimal_to_work_with}/2 with a reminder of {remainder} and bit position {bit_position}\n"
    bit_position += 1

result = resulting_number
resulting_number = resulting_number[::-1]


# Explanation
print(explanation)
print(f"Resulting number {result} should be counted backwards and we get the final result: {resulting_number}")
print(f"The binary representation of {decimal_number} is {resulting_number}")
