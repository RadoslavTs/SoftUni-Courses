current_record = float(input())
distance_record = float(input())
speed = float(input())
georgi_time = distance_record * speed
georgi_delay_1 = distance_record // 50
georgi_delay_2 = georgi_delay_1 * 30
total_time = georgi_time + georgi_delay_2
difference = abs(current_record - total_time)
total_time_result = "{:.2f}".format(total_time)
difference_result = "{:.2f}".format(difference)
if total_time < current_record:
    print(f" Yes! The new record is {total_time_result} seconds.")
elif total_time >= current_record:
    print(f"No! He was {difference_result} seconds slower.")