lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
broken_shields = 0
for sequence in range(1,lost_fights_count + 1):
    if sequence % 2 == 0:
        expenses += helmet_price
    if sequence % 3 == 0:
        expenses += sword_price
    if sequence % 3 == 0 and sequence % 2 == 0:
        expenses += shield_price
        broken_shields += 1
    if broken_shields % 2 == 0 and broken_shields != 0:
        expenses += armor_price
        broken_shields = 0
print(f"Gladiator expenses: {expenses:.2f} aureus")