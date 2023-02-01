class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    input_line = int(input())
    if input_line < 0:
        raise ValueCannotBeNegative

