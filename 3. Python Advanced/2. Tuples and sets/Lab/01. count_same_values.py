tuple_data = tuple(map(float, input().split()))
value_count = {}

for value in tuple_data:
    if value not in value_count:
        value_count[value] = 0
    value_count[value] += 1

for k, v in value_count.items():
    print(f'{k} - {v} times')