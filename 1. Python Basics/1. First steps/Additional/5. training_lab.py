length = float(input())
width = float(input())
available_width = width - 1
row_count = available_width // 0.7
column_count = length // 1.2
print(row_count)
print(column_count)
result = row_count * column_count - 3
print(result)