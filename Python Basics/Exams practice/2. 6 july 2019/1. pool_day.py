from math import ceil
people_count = int(input())
entrance_fee = float(input())
bed_price = float(input())
umbrella_price = float(input())
entrance_fee_total = people_count * entrance_fee
bed_quantity_needed = ceil(people_count * 0.75)
bed_price_total = bed_price * bed_quantity_needed
umbrellas_needed = ceil(people_count * 0.5)
umbrellas_price_total = umbrellas_needed * umbrella_price
total_cost = entrance_fee_total +  bed_price_total + umbrellas_price_total
print(f"{total_cost:.2f} lv.")
