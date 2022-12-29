rent_cost = int(input())
statues = rent_cost * 0.7
catering = statues * 0.85
music = catering / 2
total_cost = statues + catering + music + rent_cost
print(f"{total_cost:.2f}")