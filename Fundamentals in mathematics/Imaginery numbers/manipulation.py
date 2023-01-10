number_one = list(map(int, input("Въведете стойности разделени с разстояние за първото число: ").split()))
number_two = list(map(int, input("Въведете стойности разделени с разстояние за второто число: ").split()))
operation = input("изберете операция (+, -, *, /: ")
resulting_number = ''
operation_string = ''
number_one_real, number_one_imaginery = number_one[0], number_one[1]
number_two_real, number_two_imaginery = number_two[0], number_two[1]
resulting_number_real = int()
connecting_symbol = '+'
resulting_number_real = 0
resulting_number_imaginery = 0

if operation == "+":
    operation_string = 'събиране'
    resulting_number_real = number_one_real + number_two_real
    resulting_number_imaginery = number_one_imaginery + number_two_imaginery

elif operation == '-':
    operation_string = 'изваждане'
    resulting_number_real = number_one_real - number_two_real
    resulting_number_imaginery = number_one_imaginery - number_two_imaginery

elif operation == '*':
    operation_string = 'умножение'
    resulting_number_real = (number_one_real * number_two_real) + ((number_one_imaginery * number_two_imaginery) * -1)
    resulting_number_imaginery = (number_one_real * number_two_imaginery) + (number_one_imaginery * number_two_real)

elif operation == '/':
    operation_string = 'делене'
    resulting_number_top_real = ((number_one_real * number_two_real) - (number_one_imaginery * number_two_imaginery) * -1)
    resulting_number_top_imaginery = (number_one_imaginery * number_two_real) - (number_one_real * number_two_imaginery)
    resulting_number_bot_real = (number_two_real * number_two_real) - ((number_two_imaginery * number_two_imaginery) * -1)
    resulting_number_real = f"{resulting_number_top_real} / {resulting_number_bot_real}"
    resulting_number_imaginery = f"{resulting_number_top_imaginery}i / {resulting_number_bot_real}"

if operation != '/':
    if resulting_number_imaginery < 0:
        resulting_number_imaginery *= -1
        connecting_symbol = '-'

if operation == "/":
    resulting_number = f"{resulting_number_real} {connecting_symbol} {resulting_number_imaginery}"
else:
    resulting_number = f"{resulting_number_real} {connecting_symbol} {resulting_number_imaginery}i"

print(f"резултатът от операция {operation_string} на имагинерните числа е: {resulting_number}")