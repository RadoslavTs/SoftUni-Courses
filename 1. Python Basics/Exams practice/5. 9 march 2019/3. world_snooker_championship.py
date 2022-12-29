championship_level = input()
ticket_type = input()
ticket_count = int(input())
trophy_picture = input()
trophy_cost = 0
total_cost = 0
trophy_cost = 0
if championship_level == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.5
    elif ticket_type == "Premium":
        ticket_price = 105.20
    else:
        ticket_price = 118.90
elif championship_level == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    else:
        ticket_price = 300.40
else:
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    else:
        ticket_price = 400
if trophy_picture == "Y":
    trophy_cost = 40 * ticket_count
ticket_cost = ticket_price * ticket_count
if ticket_cost > 4000:
    ticket_cost *= 0.75
    trophy_cost = 0
elif ticket_cost > 2500:
    ticket_cost *= 0.9
total_cost = ticket_cost +  trophy_cost
print(f"{total_cost:.2f}")