from collections import deque

effects = deque([int(x) for x in input().split(', ')])
power = deque([int(x) for x in input().split(', ')])

palm_fireworks = 0
willow_fireworks = 0
crossette_firework = 0
show_on = False

while effects and power:
    current_effect = effects.popleft()
    current_power = power.pop()

    if current_effect <= 0:
        power.append(current_power)
        continue
    if current_power <= 0:
        effects.appendleft(current_effect)
        continue

    current_sum = current_effect + current_power

    if current_sum % 3 == 0 and current_sum % 5 == 0:
        crossette_firework += 1
    elif current_sum % 3 == 0 and current_sum % 5 != 0:
        palm_fireworks += 1
    elif current_sum % 3 != 0 and current_sum % 5 == 0:
        willow_fireworks += 1
    else:
        current_effect -= 1
        effects.append(current_effect)
        power.append(current_power)

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_firework >= 3:
        show_on = True
        break

if show_on:
    print(f"Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in effects)}")
if power:
    print(f"Explosive Power left: {', '.join(str(x) for x in power)}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_firework}")