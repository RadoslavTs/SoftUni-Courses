available_money = float(input())
sex = str(input())
if sex == "m":
    sex = "m"
elif sex == "f":
    sex = "f"
else:
    print("wrong input")
age = int(input())
sport = str(input())
difference = float()
if sport == "Gym":
    sport = "Gym"
elif sport == "Boxing":
    sport = "Boxing"
elif sport == "Yoga":
    sport = "Yoga"
elif sport == "Zumba":
    sport = "Zumba"
elif sport == "Dances":
    sport = "Dances"
elif sport == "Pilates":
    sport = "Pilates"
else:
    print("worng input")
cost= float()
if sex == "m" and age <= 19 and sport == "Gym":
    cost = 42 * 0.8
elif sex == "m" and age > 19 and sport == "Gym":
    cost = 42
elif sex == "f" and age <= 19 and sport == "Gym":
    cost = 35 * 0.8
elif sex == "f" and age <= 19 and sport == "Gym":
    cost = 35
elif sex == "m" and age <= 19 and sport == "Boxing":
    cost = 41 * 0.8
elif sex == "m" and age > 19 and sport == "Boxing":
    cost = 41
elif sex == "f" and age <= 19 and sport == "Boxing":
    cost = 37 * 0.8
elif sex == "f" and age > 19 and sport == "Boxing":
    cost = 37
elif sex == "m" and age <= 19 and sport == "Yoga":
    cost = 45 * 0.8
elif sex == "m" and age > 19 and sport == "Yoga":
    cost = 45
elif sex == "f" and age <= 19 and sport == "Yoga":
    cost = 42 * 0.8
elif sex == "f" and age > 19 and sport == "Yoga":
    cost = 42
elif sex == "m" and age <= 19 and sport == "Zumba":
    cost = 34 * 0.8
elif sex == "m" and age > 19 and sport == "Zumba":
    cost = 34
elif sex == "f" and age <= 19 and sport == "Zumba":
    cost = 31 * 0.8
elif sex == "f" and age > 19 and sport == "Zumba":
    cost = 31
elif sex == "m" and age <= 19 and sport == "Dances":
    cost = 51 * 0.8
elif sex == "m" and age > 19 and sport == "Dances":
    cost = 51
elif sex == "f" and age <= 19 and sport == "Dances":
    cost = 53 * 0.8
elif sex == "f" and age > 19 and sport == "Dances":
    cost = 53
elif sex == "m" and age <= 19 and sport == "Pilates":
    cost = 39 * 0.8
elif sex == "m" and age > 19 and sport == "Pilates":
    cost = 39
elif sex == "f" and age <= 19 and sport == "Pilates":
    cost = 37 * 0.8
elif sex == "f" and age > 19 and sport == "Pilates":
    cost = 37
difference = cost - available_money
difference_result = "{:.2f}".format(difference)
if cost < available_money:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${difference_result} more.")