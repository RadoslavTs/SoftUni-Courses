months = int(input())
total_electricity = float()
total_water = float()
total_internet = float()
total_others = float()
for sequence in range(months):
    electricity_bill = float(input())
    total_electricity += electricity_bill
    total_water += 20
    total_internet += 15
    total_others += ((electricity_bill + 20 + 15) * 0.2 + (electricity_bill + 20 + 15))
total_bills_average = (total_water + total_others + total_internet + total_electricity) / months
print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {total_bills_average:.2f} lv")
