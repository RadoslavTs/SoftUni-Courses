heritage = float(input())
year_to_live_to = int(input())
age = 17
for sequence in range(1800, year_to_live_to + 1):
    age += 1
    if sequence % 2 == 0:
        heritage -= 12000
    else:
        heritage -= 12000 + (age * 50)
if heritage >= 0:
    print(f"Yes! He will live a carefree life and will have {abs(heritage):.2f} dollars left.")
else:
    print(f"He will need {abs(heritage):.2f} dollars to survive.")
