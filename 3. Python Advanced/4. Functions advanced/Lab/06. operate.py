def operate(operator, *args):

    if operator == "+":
        return sum(args)

    elif operator == '-':
        result = args[0]
        for el in args[1:]:
            result -= el
        return result

    elif operator == '*':
        result = 1
        for el in args:
            result *= el
        return result

    elif operator == '/':
        result = args[0]
        for el in args[1:]:
            result /= el
        return result


print(operate("*", 3, 4))

