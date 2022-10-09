def palindrome(x):
    palindrome_check = True
    for sequence in range(len(x) // 2):
        check_back = -1
        if x[sequence] == x[check_back]:
            check_back -= 1
            continue
        else:
            palindrome_check = False
            break
    print(palindrome_check)


input_string = input().split(", ")
for check in input_string:
    palindrome(check)

# input_list = input().split()
# palindrome_check = True
# for number in input_list:
#     for sequence in range(len(number) // 2):
#         check_back = -1
#         first_check = number[sequence]
#         second_check = number[check_back]
#         if number[sequence] == number[check_back]:
#             check_back -= 1
#             continue
#         else:
#             palindrome_check = False
#             break
#     check_back = -1
#     print(palindrome_check)
#     palindrome_check = True
