km_quantity = int(input())
time_of_day = input()
transport_type = str()
cost = float()
if km_quantity < 20:
    transport_type = "taxi"
elif km_quantity >= 100:
    transport_type = "train"
else:
    transport_type = "bus"
if transport_type == "taxi" and time_of_day == "day":
    cost = km_quantity * 0.79 + 0.7
elif transport_type == "taxi" and time_of_day == "night":
    cost = km_quantity * 0.9 + 0.7
elif transport_type == "bus":
    cost = km_quantity * 0.09
elif transport_type == "train":
    cost = km_quantity * 0.06
print(f"{cost:.2f}")

