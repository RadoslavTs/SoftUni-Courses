def check_even(number):
    if int(number) % 2 == 0:
        return True

    return False


even_numbers = list((filter(check_even, input().split())))
even_number_int = list(map(int, even_numbers))
print(even_number_int)
