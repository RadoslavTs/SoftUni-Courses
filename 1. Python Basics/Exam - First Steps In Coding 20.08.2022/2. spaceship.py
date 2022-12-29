from math import(floor)
ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
astronaut_mean_height = float(input())
ship_volume = ship_height * ship_length * ship_width
room_volume = (astronaut_mean_height + 0.4) * 4
crew_capacity = floor(ship_volume / room_volume)
if 10 >= crew_capacity >= 3:
    print(f"The spacecraft holds {crew_capacity} astronauts.")
elif crew_capacity < 3:
    print(f"The spacecraft is too small.")
else:
    print("The spacecraft is too big.")