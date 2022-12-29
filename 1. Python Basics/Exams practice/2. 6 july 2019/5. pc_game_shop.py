sold_games = int(input())
hearthstone_sold = 0
fornite_sold = 0
overwatch_sold = 0
others_sold = 0
for sequence in range(sold_games):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_sold += 1
    elif game_name == "Fornite":
        fornite_sold += 1
    elif game_name == "Overwatch":
        overwatch_sold += 1
    else:
        others_sold += 1
hearthstone_perc = hearthstone_sold / sold_games * 100
fornite_perc = fornite_sold / sold_games * 100
overwatch_perc = overwatch_sold / sold_games * 100
others_perc = others_sold / sold_games * 100
print(f"Hearthstone - {hearthstone_perc:.2f}%")
print(f"Fornite - {fornite_perc:.2f}%")
print(f"Overwatch - {overwatch_perc:.2f}%")
print(f"Others - {others_perc:.2f}%")