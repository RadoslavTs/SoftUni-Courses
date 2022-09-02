import sys
number = int(input())
sum = int()
max_number = -sys.maxsize
for sequence in range(number):
    human_input = int(input())
    sum += human_input
    if human_input > max_number:
        max_number = human_input
if sum - max_number == max_number:
        print("Yes")
        print(f"Sum = {max_number}")
else:
    difference = abs(max_number - (sum - max_number))
    print("No")
    print(f"Diff = {difference}")