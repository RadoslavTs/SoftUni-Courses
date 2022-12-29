name_list = input().split(", ")
sorted_list = sorted(name_list, key = lambda item: (-len(item), item))
print(sorted_list)