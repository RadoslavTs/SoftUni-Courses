box_of_clothes = list(map(int, input().split()))
rack_capacity = int(input())
current_rack = rack_capacity
racks_used = 1

while box_of_clothes:
    cloth = box_of_clothes.pop()

    if current_rack - cloth >= 0:
        current_rack -= cloth

    else:
        racks_used += 1
        current_rack = rack_capacity - cloth

print(racks_used)
