from collections import deque

milligrams = deque(list(map(int, input().split(', '))))

energy_drinks = deque(list(map(int, input().split(', '))))

caffeine_consumed = 0
max_caffeine = 300

while milligrams and energy_drinks:
    current_milligrams = milligrams.pop()
    current_energy_drink = energy_drinks.popleft()
    current_sum = current_milligrams * current_energy_drink
    if current_sum + caffeine_consumed <= max_caffeine:
        caffeine_consumed += current_sum
    else:
        energy_drinks.append(current_energy_drink)
        caffeine_consumed -= 30
        if caffeine_consumed < 0:
            caffeine_consumed = 0


if energy_drinks:
    print(f"Drinks left: ", end='')
    print(*list(energy_drinks), sep=', ')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {caffeine_consumed} mg caffeine.")
