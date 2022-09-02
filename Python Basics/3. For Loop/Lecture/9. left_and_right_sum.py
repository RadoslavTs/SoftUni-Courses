number = int(input())
left_sum = 0
right_sum = 0
for sequence in range(number * 2):
    from_human = int(input())
    if sequence < number:
        left_sum += from_human
    else:
        right_sum += from_human
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")