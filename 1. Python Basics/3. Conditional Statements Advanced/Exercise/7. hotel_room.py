month = input()
stay_length = int(input())
apartment_price = float()
studio_price = float()
cost = float()
if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
elif month == "June" or month == "September":
    studio_price = 75.2
    apartment_price = 68.70
else:
    studio_price = 76
    apartment_price = 77
if stay_length > 7 and stay_length <= 14 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.95
elif stay_length > 14 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.7
elif stay_length > 14 and (month == "June" or month == "September"):
    studio_price = studio_price * 0.8
if stay_length > 14:
    apartment_price = apartment_price * 0.9
cost_studio = stay_length * studio_price
cost_apartment = stay_length * apartment_price
print(f"Apartment: {cost_apartment:.2f} lv.")
print(f"Studio: {cost_studio:.2f} lv.")