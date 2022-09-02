count = int(input())
previous_sum = int(input()) + int(input())
max_difference = 0
for sequence in range(count - 1):
    current_sum = int(input()) + int(input())
    sum_abs = abs(previous_sum - current_sum)
    if sum_abs > max_difference:
        max_difference = sum_abs
    previous_sum = current_sum

if max_difference == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_difference}")
