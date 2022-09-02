# divisor = int(input())
# boundary = int(input())
# largest_number = int()
# for sequence in range(boundary + 1):
#     if sequence % divisor == 0 and sequence <= boundary and sequence != 0:
#         if sequence > largest_number:
#             largest_number = sequence
# print(largest_number)

divisor = int(input())
boundary = int(input())
largest_number = int()
for sequence in range(boundary, divisor, -1):
    if sequence % divisor == 0:
        largest_number = sequence
        break
print(largest_number)