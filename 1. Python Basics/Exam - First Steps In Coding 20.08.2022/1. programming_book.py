price_per_page = float(input())
price_per_cover = float(input())
percent_discount = int(input())
design_cost = float(input())
share_of_team = int(input())
initial_sum = (price_per_page * 899) + (price_per_cover * 2)
discount_sum = initial_sum * percent_discount / 100
total_sum = initial_sum - discount_sum + design_cost
finam_cost = total_sum * (1 - (share_of_team / 100))
print(f"Avtonom should pay {finam_cost:.2f} BGN.")