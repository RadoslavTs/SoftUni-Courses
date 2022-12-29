low_range = int(input())
high_range = int(input())
first_digit_flag = False
second_digit_flag = False
third_digit_flag = False
fourth_digit_flag = False
first_digit = 0
second_digit = 0
third_digit = 0
fourth_digit = 0
for sequence in range(low_range, high_range + 1):
    for index, value in enumerate(str(sequence)):
        if index == 0 and int(value) % 2 != 0 and int(value) <= int(str(high_range)[0]) and int(value) >= int(str(low_range)[0]):
            first_digit_flag = True
            first_digit = value
        if index == 1 and int(value) % 2 != 0 and int(value) <= int(str(high_range)[1]) and int(value) >= int(str(low_range)[1]):
            second_digit_flag = True
            second_digit = value
        if index == 2 and int(value) % 2 != 0 and int(value) <= int(str(high_range)[2]) and int(value) >= int(str(low_range)[2]):
            third_digit_flag = True
            third_digit = value
        if index == 3 and int(value) % 2 != 0 and int(value) <= int(str(high_range)[3]) and int(value) >= int(str(low_range)[3]):
            fourth_digit_flag = True
            fourth_digit = value
        if first_digit_flag and second_digit_flag and third_digit_flag and fourth_digit_flag:
            print(f"{first_digit}{second_digit}{third_digit}{fourth_digit}", end = ' ')
    first_digit = 0
    second_digit = 0
    third_digit = 0
    fourth_digit = 0
    first_digit_flag = False
    second_digit_flag = False
    third_digit_flag = False
    fourth_digit_flag = False