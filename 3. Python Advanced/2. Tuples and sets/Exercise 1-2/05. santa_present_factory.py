from collections import deque

materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

matching_pair_one = {'Doll', 'Wooden train'}
matching_pair_two = {'Teddy bear', 'Bicycle'}

magic_dict = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
crafted_presents = {}

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    current_points = current_material * current_magic
    if current_points in magic_dict.keys():
        current_toy = magic_dict[current_points]
        if current_toy not in crafted_presents.keys():
            crafted_presents[current_toy] = 1
        else:
            crafted_presents[current_toy] += 1

        if current_toy in matching_pair_one:
            matching_pair_one.discard(current_toy)
        elif current_toy in matching_pair_two:
            matching_pair_two.discard(current_toy)

    elif current_points < 0:
        resulting_points = current_material + current_magic
        materials.append(resulting_points)
    elif current_points > 0:
        materials.append(current_material + 15)
    elif current_material == 0 or current_magic == 0:
        if current_material == 0 and current_magic != 0:
            magic_level.appendleft(current_magic)
        elif current_material != 0 and current_magic == 0:
            materials.append(current_material)
        elif current_material == 0 and current_magic == 0:
            continue

if not matching_pair_one or not matching_pair_two:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

materials_list = reversed(materials)

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials_list)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for present, quantity in sorted(crafted_presents.items()):
    print(f"{present}: {quantity}")
