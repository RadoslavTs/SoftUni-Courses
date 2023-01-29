input_list = [string.split() for string in input().split("|")]
print(*[' '.join(string) for string in input_list[::-1] if string])
