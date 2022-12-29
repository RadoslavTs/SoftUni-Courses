walk_duration = int(input())
walk_number = int(input())
calorie_intake = int(input())
calories_burnt = walk_duration * walk_number * 5
calorie_intake = calorie_intake * 0.5
if calories_burnt >= calorie_intake:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burnt}.")
elif calories_burnt < calorie_intake:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burnt}.")