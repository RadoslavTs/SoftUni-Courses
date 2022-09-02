import math
absence_duration = int(input())
food_left = int(input())
dog_food_needed = float(input())
cat_food_needed = float(input())
turtle_food_needed = float(input())
dog_food_consumed = dog_food_needed * absence_duration
cat_food_consumed = cat_food_needed * absence_duration
turtle_food_consumed = turtle_food_needed * absence_duration / 1000
total_food_needed = dog_food_consumed + cat_food_consumed + turtle_food_consumed
difference = food_left - total_food_needed
if total_food_needed <= food_left:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil(abs(difference))} more kilos of food are needed.")