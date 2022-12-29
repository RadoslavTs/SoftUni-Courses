decoration_count = int(input())
days_until_christmas = int(input())
total_cost = 0
christmas_spirit = 0
ornament_set = 2
tree_skirt = 5
tree_gerland = 3
tree_lights = 15
for sequence in range(1, days_until_christmas + 1):
    if sequence % 11 == 0:
        decoration_count += 2
    if sequence % 2 == 0:
        total_cost += ornament_set * decoration_count
        christmas_spirit += 5
    if sequence % 3 == 0:
        total_cost += (tree_skirt + tree_gerland) * decoration_count
        christmas_spirit += 13
    if sequence % 5 == 0:
        christmas_spirit += 17
        total_cost += tree_lights * decoration_count
        if sequence % 3 == 0:
            christmas_spirit += 30
    if sequence % 10 == 0:
        christmas_spirit -= 20
        total_cost += tree_skirt + tree_gerland + tree_lights
if days_until_christmas % 10 == 0:
    christmas_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")



