from math import ceil
people_to_carry = int(input())
elevator_capacity = int(input())
trips_needed = people_to_carry / elevator_capacity
print(ceil(trips_needed))