input_list = list(map(int, input().split(", ")))
if max(input_list) % 10 == 0:
    max_value = max(input_list) // 10
else:
    max_value = max(input_list) // 10 + 1
for sequence in range(1, max_value + 1):
    group = [num for num in input_list if num <= sequence * 10 if num > sequence * 10 - 10]
    print(f"Group of {sequence*10}'s: {group}")