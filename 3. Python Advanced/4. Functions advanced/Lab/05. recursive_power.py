def recursive_power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a

    return a * recursive_power(a, b-1)


print(recursive_power(2, 10))

#
# def recursive_power(a, b):
#     result = a
#     limit = b
#     if b == 1:
#         return a
#     elif b == 1:
#         return 1
#     else:
#         while limit > 1:
#             result *= a
#             limit -= 1
#         return result


print(recursive_power(10, 100))