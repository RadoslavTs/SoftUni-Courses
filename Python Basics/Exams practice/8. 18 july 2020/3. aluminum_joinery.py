window_count = int(input())
window_type = str(input())
delivery = str(input())
window_price = float()
total_cost_before_discount = float()
transport_cost = float()
if window_count < 10:
    print("Invalid order")
if window_type == "90X130" and window_count <= 30:
    window_price = 110
elif window_type == "90X130" and window_count <= 60:
    window_price = 110 * 0.95
elif window_type == "90X130" and window_count > 60:
    window_price = 110 * 0.92
elif window_type == "100X150" and window_count <= 40:
    window_price = 140
elif window_type == "100X150" and window_count < 80:
    window_price = 140 * 0.94
elif window_type == "100X150" and window_count > 80:
    window_price = 140 * 0.90
elif window_type == "130X180" and window_count <= 20:
    window_price = 190
elif window_type == "130X180" and window_count < 50:
    window_price = 190 * 0.93
elif window_type == "130X180" and window_count > 50:
    window_price = 190 * 0.88
elif window_type == "200X300" and window_count <= 25:
    window_price = 250
elif window_type == "200X300" and window_count < 50:
    window_price = 250 * 0.91
elif window_type == "200X300" and window_count > 50:
    window_price = 250 * 0.86
total_cost_before_discount = window_count * window_price + transport_cost
if delivery == "With delivery":
    transport_cost = 60
elif delivery == "Without delivery":
    transport_cost = 0
if window_count >= 99:
    total_cost_before_discount = (total_cost_before_discount + transport_cost) * 0.96
else:
    total_cost_before_discount = total_cost_before_discount + transport_cost
if window_count >= 10:
    print(f"{total_cost_before_discount:.2f} BGN")


