trip_cost = float(input())
puzzle_count = int(input())
talking_dolls_count = int(input())
teddy_bear_count = int(input())
minions_count = int(input())
trucks_count = int(input())
total_toys_count = puzzle_count + talking_dolls_count + teddy_bear_count + minions_count + trucks_count
puzzle_income = puzzle_count * 2.60
talking_dolls_income = talking_dolls_count * 3
teddy_bear_income = teddy_bear_count * 4.10
minions_income = minions_count * 8.20
trucks_income = trucks_count * 2
total_income = puzzle_income + talking_dolls_income + teddy_bear_income + minions_income + trucks_income
if total_toys_count >= 50:
    total_income = total_income * 0.75
shop_rent = total_income *0.1
total_income = total_income - shop_rent
money_leftover = trip_cost - total_income
if total_income >= trip_cost:
    print(f"Yes! {abs(money_leftover):.2f} lv left.")
else:
    print(f"Not enough money! {abs(money_leftover):.2f} lv needed.")