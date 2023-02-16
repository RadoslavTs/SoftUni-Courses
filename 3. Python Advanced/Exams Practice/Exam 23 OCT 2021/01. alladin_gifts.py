from collections import deque


def make_gift(sums):
    global gemstones
    global porcelain_sculptures
    global gold
    global diamond_jewellery

    if 100 <= sums <= 199:
        gemstones += 1

    elif 200 <= sums <= 299:
        porcelain_sculptures += 1

    elif 300 <= sums <= 399:
        gold += 1

    elif 400 <= sums <= 499:
        diamond_jewellery += 1


def under_100(mat, mag):
    if current_sum % 2 == 0:
        mat *= 2
        mag *= 3
        return mat + mag
    else:
        return current_sum * 2


materials = deque(input().split())
magic_levels = deque(input().split())

gemstones = 0
porcelain_sculptures = 0
gold = 0
diamond_jewellery = 0

while materials and magic_levels:
    current_material = int(materials.pop())
    current_magic = int(magic_levels.popleft())
    current_sum = current_material + current_magic
    if current_sum < 100:
        current_sum = under_100(current_material, current_magic)
    if current_sum > 499:
        current_sum /= 2

    make_gift(current_sum)


if (gemstones and porcelain_sculptures) or (gold and diamond_jewellery):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

if diamond_jewellery:
    print(f"Diamond Jewellery: {diamond_jewellery}")
if gemstones:
    print(f"Gemstone: {gemstones}")
if gold:
    print(f"Gold: {gold}")
if porcelain_sculptures:
    print(f"Porcelain Sculpture: {porcelain_sculptures}")


