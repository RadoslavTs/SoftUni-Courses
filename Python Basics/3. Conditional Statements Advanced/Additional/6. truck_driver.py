season = input()
monthly_km = float(input())
lv_km = float()
salary = float()
if monthly_km <= 5000:
    if season == "Spring" or season == "Autumn":
        lv_km = 0.75
    elif season == "Summer":
        lv_km = 0.9
    else:
        lv_km = 1.05
elif monthly_km > 5000 and monthly_km <= 10000:
    if season == "Spring" or season == "Autumn":
        lv_km = 0.95
    elif season == "Summer":
        lv_km = 1.1
    else:
        lv_km = 1.25
else:
    lv_km = 1.45
salary = lv_km * monthly_km * 4 * 0.9
print(f"{salary:.2f}")