# def rounding(n):
#     return round(n)
#
#
# input_string = input().split()
# input_list = list(map(float, input_string))
# output_list = list(map(rounding, input_list))
# print(output_list)

print(list(map(lambda x: round(float(x)), input().split())))