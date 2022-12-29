number_of_fills = int(input())
capacity = 255
filling_water = 0
total_water_filled = 0
for sequence in range(number_of_fills):
    filling_water = int(input())
    if filling_water > capacity:
        print("Insufficient capacity!")
    else:
        capacity -= filling_water
        total_water_filled += filling_water
print(total_water_filled)
