def triangle(a):
    result = ''
    for _ in range(1, a + 1):
        for i in range(1, _ + 1):
            result += str(i) + " "
        result += '\n'

    for _ in range(a, 0, -1):
        for i in range(1, _):
            result += str(i) + " "
        result += '\n'

    return result