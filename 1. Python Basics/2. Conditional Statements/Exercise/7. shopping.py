budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())
video_cards_cost = video_cards_count * 250
processors_cost = processors_count * video_cards_cost * 0.35
ram_memory_cost = ram_memory_count * video_cards_cost * 0.1
total_cost = video_cards_cost + processors_cost + ram_memory_cost
if video_cards_count > processors_count:
    total_cost = total_cost * 0.85
difference = budget - total_cost
if budget >= total_cost:
    print(f"You have {abs(difference):.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(difference):.2f} leva more!")