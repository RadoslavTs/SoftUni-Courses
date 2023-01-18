from collections import deque

cup_capacity = deque(int(cup) for cup in input().split())
bottle_capacity = deque(int(bottle) for bottle in input().split())
wasted_water = 0

while True:
    if not cup_capacity:
        break
    if not bottle_capacity:
        break
    current_cup = cup_capacity.popleft()
    current_bottle = bottle_capacity.pop()
    if current_cup - current_bottle <= 0:
        wasted_water += abs(current_cup - current_bottle)
    else:
        cup_capacity.appendleft(current_cup-current_bottle)

if not cup_capacity:
    print(f"Bottles: {' '.join(map(str, bottle_capacity))}")
else:
    print(f"Cups: {' '.join(map(str, cup_capacity))}")
print(f'Wasted litters of water: {wasted_water}')
