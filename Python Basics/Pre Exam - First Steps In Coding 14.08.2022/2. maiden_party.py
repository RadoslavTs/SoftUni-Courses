maiden_party_cost = float(input())
love_letters_count = int(input())
wax_roses_count = int(input())
key_chains_count = int(input())
frames_count = int(input())
surprises_count = int(input())
love_letters_cost = love_letters_count * 0.6
wax_roses_cost = wax_roses_count * 7.2
key_chains_cost = key_chains_count * 3.6
frames_cost = frames_count * 18.2
surprises_cost = surprises_count * 22
total_items_cost = love_letters_cost + wax_roses_cost + key_chains_cost + frames_cost + surprises_cost
total_items = love_letters_count + wax_roses_count + key_chains_count + frames_count + surprises_count
if total_items > 25:
    total_items_cost *= 0.65
hosting_cost = total_items_cost * 0.1
earnings = total_items_cost - hosting_cost
difference = abs(earnings - maiden_party_cost)
if earnings > maiden_party_cost:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")