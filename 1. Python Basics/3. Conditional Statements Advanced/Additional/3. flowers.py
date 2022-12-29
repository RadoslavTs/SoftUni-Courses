hrisantems = int(input())
rose = int(input())
tulips = int(input())
season = input()
holiday = input()
hrisantems_price = float()
roses_price = float()
tulips_price = float()
holiday_flag = False
holiday_markup = 1
discount_tulips = 1
discount_rose = 1
discount_all = 1
buqet_price = 0
total_flowers = hrisantems + rose + tulips
if holiday == "Y":
    holiday_flag = True
if holiday_flag:
    holiday_markup = 1.15
if season == "Spring" or season == "Summer":
    hrisantems_price = 2
    roses_price = 4.1
    tulips_price = 2.5
else:
    hrisantems_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15
buqet_price = hrisantems_price * hrisantems + rose * roses_price + tulips_price * tulips
buqet_price = buqet_price * holiday_markup
if tulips > 7 and season == "Spring":
    discount_tulips = 0.95
if rose >= 10 and season == "Winter":
    discount_rose = 0.9
if total_flowers > 20:
    discount_all = 0.8
buqet_price = buqet_price * discount_tulips
buqet_price = buqet_price * discount_rose
buqet_price = buqet_price * discount_all
buqet_price = buqet_price + 2
print(f"{buqet_price:.2f}")
