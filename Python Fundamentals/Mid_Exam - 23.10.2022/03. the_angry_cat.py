price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
price = input()
left_sum = 0
right_sum = 0
for left_side in range(0, entry_point):
    if price == "cheap":
        if price_ratings[left_side] < price_ratings[entry_point]:
            left_sum += price_ratings[left_side]
    if price == "expensive":
        if price_ratings[left_side] >= price_ratings[entry_point]:
            left_sum += price_ratings[left_side]
for right_side in range(entry_point + 1, len(price_ratings)):
    if price == "cheap":
        if price_ratings[right_side] < price_ratings[entry_point]:
            right_sum += price_ratings[right_side]
    if price == "expensive":
        if price_ratings[right_side] >= price_ratings[entry_point]:
            right_sum += price_ratings[right_side]
if left_sum >= right_sum:
    print(f"Left - {left_sum}")
else:
    print(f"Right - {right_sum}")
