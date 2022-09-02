baggage_cost_over_twenty = float(input())
baggage_kg = float(input())
travel_days = int(input())
baggage_count = int(input())
real_baggage_cost = float()
cost = float()
if baggage_kg < 10:
    real_baggage_cost = baggage_cost_over_twenty * 0.2
elif baggage_kg <= 20:
    real_baggage_cost = baggage_cost_over_twenty * 0.5
else:
    real_baggage_cost = baggage_cost_over_twenty
if travel_days > 30:
    real_baggage_cost = real_baggage_cost * 1.1
elif travel_days >= 7:
    real_baggage_cost = real_baggage_cost * 1.15
else:
    real_baggage_cost = real_baggage_cost * 1.4
cost = real_baggage_cost *baggage_count
result = "{:.2f}".format(cost)
print(f" The total price of bags is: {result} lv. ")