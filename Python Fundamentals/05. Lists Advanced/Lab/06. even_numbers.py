input_list = list(map(int, input().split(", ")))
indices = [num for num in range(len(input_list)) if input_list[num] % 2 == 0]
print(indices)