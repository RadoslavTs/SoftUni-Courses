import math

show_name = input()
show_length = int(input())
break_length = int(input())
# time_left = float()
lunch_time = break_length / 8
rest_time = break_length / 4
time_left = break_length - lunch_time - rest_time
time_differencec = abs(show_length - time_left)
if time_left >= show_length:
    print(f"You have enough time to watch {show_name} and left with {math.ceil(time_differencec)} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {math.ceil(time_differencec)} more minutes.")