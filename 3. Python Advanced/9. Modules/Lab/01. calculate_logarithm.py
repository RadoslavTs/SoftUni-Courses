from math import log


def log_function(x, base):
    if base == "natural":
        result = f'{log(x):.2f}'
    else:
        result = f'{log(x, int(base)):.2f}'

    return result


number_to_convert = int(input())
base_type = input()


print(log_function(number_to_convert, base_type))