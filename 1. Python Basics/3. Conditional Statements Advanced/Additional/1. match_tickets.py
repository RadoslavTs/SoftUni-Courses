budget = float(input())
category = input()
people_count = int(input())
transport_cost = float()
ticket_cost = float()
difference = 0
total_cost = 0
if people_count <= 4:
    transport_cost = budget * 0.75
elif people_count <= 9:
    transport_cost = budget * 0.6
elif people_count <= 24:
    transport_cost = budget * 0.5
elif people_count <= 49:
    transport_cost = budget * 0.4
else:
    transport_cost = budget * 0.25
if category == "VIP":
    ticket_cost = 499.99
else:
    ticket_cost = 249.99
total_cost = transport_cost + (people_count * ticket_cost)
difference = budget - total_cost
if difference >= 0:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(difference):.2f} leva.")
