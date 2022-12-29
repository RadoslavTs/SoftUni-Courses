input_string = input()
count = int(input())
repeat_string = lambda a, b: a * b
result = repeat_string(input_string, count)
print(result)