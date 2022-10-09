def validation(x):
    digits_count = 0
    if 10 >= len(x) >= 6:
        character_check = True
        digits_count = 0
        for sequence in range(len(x)):
            if 48 <= ord(x[sequence]) <= 57:
                digits_count += 1
            if (48 <= ord(x[sequence]) <= 57) or (65 <= ord(x[sequence]) <= 90) or (97 <= ord(x[sequence]) <= 122):
                continue
            else:
                character_check = False
        if not character_check:
            print("Password must consist only of letters and digits")
        if digits_count > 2 and character_check:
            print("Password is valid")
    else:
        print("Password must be between 6 and 10 characters")
    if digits_count < 2:
        print("Password must have at least 2 digits")



validation(input())
