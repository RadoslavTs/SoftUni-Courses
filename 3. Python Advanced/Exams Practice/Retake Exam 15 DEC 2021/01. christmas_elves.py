from collections import deque

elfs_energy = deque(int(x) for x in input().split())
materials_in_box = [int(x) for x in input().split()]

info = {
    "toys": 0,
    "energy spend": 0,
    "counter": 0
}


def make_toys(energy, box, toys):
    elfs_energy.append(energy - (box - 1))
    info["toys"] += toys
    info["energy spend"] += box


def every_third_time(energy, box):
    make_toys(energy, box, 2)


def every_fifth_time(energy, box):
    elfs_energy.append(energy - box)
    info["energy spend"] += box


def not_enough_energy(energy, box):
    elfs_energy.append(energy * 2)
    materials_in_box.append(box)


def multiply_turns(current_elf, current_box, current_time, adding_box=False):
    multiply_box = current_box
    if adding_box:
        multiply_box = current_box * 2
    if current_elf >= multiply_box:
        if current_time == 5:
            every_fifth_time(current_elf, multiply_box)
        elif current_time == 3:
            every_third_time(current_elf, multiply_box)
    else:
        not_enough_energy(current_elf, current_box)


while elfs_energy and materials_in_box:
    energy = elfs_energy.popleft()
    if energy < 5:
        continue

    info["counter"] += 1
    box = materials_in_box.pop()

    if info["counter"] % 3 == 0 and info["counter"] % 5 == 0:
        multiply_turns(energy, box, 5, True)

    elif info["counter"] % 3 == 0:
        multiply_turns(energy, box, 3, True)

    elif info["counter"] % 5 == 0:
        multiply_turns(energy, box, 5)

    elif box > energy:
        not_enough_energy(energy, box)

    else:
        make_toys(energy, box, 1)

print(f"Toys: {info['toys']}")
print(f"Energy: {info['energy spend']}")
if elfs_energy:
    print(f"Elves left: {', '.join(str(x) for x in elfs_energy)}")
if materials_in_box:
    print(f"Boxes left: {', '.join(str(x) for x in materials_in_box)}")