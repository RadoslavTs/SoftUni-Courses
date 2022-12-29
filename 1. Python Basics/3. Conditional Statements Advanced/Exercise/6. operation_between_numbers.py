first_digit = int(input())
second_digit = int(input())
operand = input()
result = float()
zero_flag = False
even_or_odd = str
if operand == "+":
    result = first_digit + second_digit
elif operand == "-":
    result = first_digit - second_digit
elif operand == "*":
    result = first_digit * second_digit
elif operand == "/":
    if second_digit == 0:
        zero_flag = True
    else:
        result = first_digit / second_digit
else:
    if second_digit == 0:
        zero_flag = True
    else:
        result = first_digit % second_digit
if zero_flag:
    print(f"Cannot divide {first_digit} by zero")
elif operand == "+" or operand == "-" or operand == "*":
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_digit} {operand} {second_digit} = {result} - {even_or_odd}")
elif operand == "/":
    print(f"{first_digit} / {second_digit} = {result:.2f}")
else:
    print(f"{first_digit} % {second_digit} = {result}")