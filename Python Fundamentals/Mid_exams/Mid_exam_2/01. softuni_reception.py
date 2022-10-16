from math import ceil
first_clerk_efficiency = int(input())
second_clerk_efficiency = int(input())
third_clerk_efficiency = int(input())
students_count = int(input())
total_clerk_efficiency = first_clerk_efficiency + second_clerk_efficiency + third_clerk_efficiency
time_needed_before_breaks = students_count / total_clerk_efficiency
breaks = time_needed_before_breaks // 3
total_time_needed = ceil(time_needed_before_breaks) + breaks
print(f"Time needed: {total_time_needed:.0f}h.")

