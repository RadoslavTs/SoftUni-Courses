from math import floor
current_record = float(input())
swimming_distance = float(input())
swim_speed_for_one_meter = float(input())
swim_time = swim_speed_for_one_meter * swimming_distance
delay_time = floor(swimming_distance / 15) * 12.5
total_swim_time = swim_time + delay_time
missing_time = current_record - total_swim_time
if total_swim_time < current_record:
    print(f"Yes, he succeeded! The new world record is {abs(total_swim_time):.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(missing_time):.2f} seconds slower.")