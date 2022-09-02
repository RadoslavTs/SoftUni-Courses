number = int(input())
first_digit = 0
second_digit = 0
third_digit = 0
fourth_digit = 0
first_digit_flag = False
second_digit_flag = False
third_digit_flag = False
fourth_digit_flag = False
special_number = 0
for sequence in range(1111, 10000):
    for index, digit in enumerate(str(sequence)):
        if int(digit) != 0:
            if index == 0 and number % int(digit) == 0:
                first_digit = int(digit)
                first_digit_flag = True
            if index == 1 and number % int(digit) == 0:
                second_digit = int(digit)
                second_digit_flag = True
            if index == 2 and number % int(digit) == 0:
                third_digit = int(digit)
                third_digit_flag = True
            if index == 3 and number % int(digit) == 0:
                fourth_digit = int(digit)
                fourth_digit_flag = True
            if first_digit_flag and second_digit_flag and third_digit_flag and fourth_digit_flag:
                print(f"{first_digit}{second_digit}{third_digit}{fourth_digit}", end=" ")
                first_digit = 0
                second_digit = 0
                third_digit = 0
                fourth_digit = 0
                first_digit_flag = False
                second_digit_flag = False
                third_digit_flag = False
                fourth_digit_flag = False
    first_digit = 0
    second_digit = 0
    third_digit = 0
    fourth_digit = 0
    first_digit_flag = False
    second_digit_flag = False
    third_digit_flag = False
    fourth_digit_flag = False
