number = int(input())
sequence_qty = int()
if number == 1:
    sequence_qty = 1
else:
    sequence_qty = number * 2 - 1
for i in range(1, sequence_qty + 1):
    if i <= number:
        print(" " * (number - i) + "* " * i)
    else:
        print(" " * (i - number) + "* " * (sequence_qty + 1 - i))