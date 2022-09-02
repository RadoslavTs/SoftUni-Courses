import sys
number = int(input())
min_number = sys.maxsize
max_number = -sys.maxsize
for quantity in range(1, number + 1, 1):
    result = int(input())
    if result > max_number:
        max_number = result
    if result < min_number:
        min_number = result
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")