deposit = float(input())
srok = float(input())
interest = float(input())
accumulated_interest = deposit * interest / 100
daily_interest = accumulated_interest / 12
suma = deposit + srok * daily_interest
print(suma)