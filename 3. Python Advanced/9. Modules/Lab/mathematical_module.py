import operator as op

def math_operations(input_string):
    input_split = input_string.split()
    number_one = float(input_split[0])
    number_two = int(input_split[2])
    operator_sign = input_split[1]
    valid_operators = {
        '*': op.mul,
        '/': op.truediv,
        '-': op.sub,
        '+': op.add,
        '^': op.pow
    }

    return valid_operators[operator_sign](number_one, number_two)
