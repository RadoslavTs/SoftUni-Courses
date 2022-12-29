def password_validation(some_password):
    pass_is_valid = True
    if len(some_password) < 6 or len(some_password) > 10:
        print("Password must be between 6 and 10 characters")
        pass_is_valid = False
    if not some_password.isalnum():
        print("Password must consist only of letters and digits")
        pass_is_valid = False
    digits_countr = 0
    for character in some_password:
        if character.isdigit():
            digits_countr += 1
    if digits_countr < 2:
        print("Password must have at least 2 digits")
        pass_is_valid = False

    return pass_is_valid


password = input()
password_is_valid = password_validation(password)
if password_is_valid:
    print("Password is valid")





# def length(word):
#     if 10 >= len(word) >= 6:
#         return True
#     else:
#         return False
#
#
# def digits_count(word):
#     digits = 0
#     for digit in word:
#         if 48 <= ord(digit) <= 57:
#             digits += 1
#     if digits >= 2:
#         return True
#     else:
#         return False
#
#
# def letter_digit_check(word):
#     check_value = True
#     for digital in word:
#         ord_value = ord(digital)
#         if (48 <= ord_value <= 57) or (65 <= ord_value <= 90) or (97 <= ord_value <= 122):
#             check_value = True
#         else:
#             check_value = False
#             break
#     return check_value
#
#
# string = input()
# length_check = length(string)
# two_digits_check = digits_count(string)
# letter_and_digits_check = letter_digit_check(string)
#
# if length_check and two_digits_check and letter_and_digits_check:
#     print("Password is valid")
# else:
#     if not length_check:
#         print("Password must be between 6 and 10 characters")
#     if not letter_and_digits_check:
#         print("Password must consist only of letters and digits")
#     if not two_digits_check:
#         print("Password must have at least 2 digits")
