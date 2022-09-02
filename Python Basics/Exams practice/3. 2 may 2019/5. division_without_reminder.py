number_range = int(input())
p1_count = 0
p2_count = 0
p3_count = 0
for sequence in range(number_range):
    current_number = int(input())
    if current_number % 2 == 0:
        p1_count += 1
    if current_number % 3 == 0:
        p2_count += 1
    if current_number % 4 == 0:
        p3_count += 1
p1_perc = p1_count / number_range * 100
p2_perc = p2_count / number_range * 100
p3_perc = p3_count / number_range * 100
print(f"{p1_perc:.2f}%")
print(f"{p2_perc:.2f}%")
print(f"{p3_perc:.2f}%")