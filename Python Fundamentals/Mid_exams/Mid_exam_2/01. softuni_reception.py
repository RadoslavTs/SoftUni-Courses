first_clerk_efficiency = int(input())
second_clerk_efficiency = int(input())
third_clerk_efficiency = int(input())
students_count = int(input())
clerk_efficiency_min = 60 / (first_clerk_efficiency + second_clerk_efficiency + third_clerk_efficiency)
time_needed_before_breaks = students_count * clerk_efficiency_min
breaks = time_needed_before_breaks // 180
break_time = breaks * 60
total_time_needed = (time_needed_before_breaks + break_time) // 60
left_over = (time_needed_before_breaks + break_time) % 60
if left_over > 0:
    total_time_needed += 1
print(f"Time needed: {total_time_needed:.0f}h.")