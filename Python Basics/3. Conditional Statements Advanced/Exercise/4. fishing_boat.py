budget = int(input())
season = input()
fisherman_number = int(input())
boat_rent = float()
discount = float()
difference = float()
if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
else:
    boat_rent = 2600
if fisherman_number <= 6:
    boat_rent = boat_rent * 0.9
elif 7 <= fisherman_number <= 11:
    boat_rent = boat_rent *0.85
else:
    boat_rent = boat_rent * 0.75
if fisherman_number % 2 == 0 and season != "Autumn":
    boat_rent = boat_rent * 0.95
difference = abs(budget - boat_rent)
if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")