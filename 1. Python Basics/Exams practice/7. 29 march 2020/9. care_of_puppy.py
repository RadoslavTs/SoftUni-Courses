food_bought = int(input())
food_bought = food_bought * 1000
food_for_the_day = ""
while food_for_the_day != "Adopted":
    food_for_the_day = input()
    if food_for_the_day == "Adopted":
        break
    food_bought -= int(food_for_the_day)
if food_bought >= 0:
    print(f"Food is enough! Leftovers: {food_bought} grams.")
else:
    print(f"Food is not enough. You need {abs(food_bought)} grams more.")
