level_of_fire = input().split("#")
available_water = int(input())
effort = int()
final_cells = []
total_fire = 0
for level in level_of_fire:
    current_level = level.split(" = ")
    current_level_key = current_level[0]
    current_level_value = int(current_level[1])
    if current_level_key == "High":
        if current_level_value < 81 or current_level_value > 125:
            pass
        else:
            if available_water < current_level_value:
                pass
            else:
                available_water -= current_level_value
                effort += 0.25 * current_level_value
                final_cells.append(current_level_value)
    elif current_level_key == "Medium":
        if current_level_value < 51 or current_level_value > 80:
            pass
        else:
            if available_water < current_level_value:
                pass
            else:
                available_water -= current_level_value
                effort += 0.25 * current_level_value
                final_cells.append(current_level_value)
    else:
        if current_level_value < 1 or current_level_value > 50:
            pass
        else:
            if available_water < current_level_value:
                pass
            else:
                available_water -= current_level_value
                effort += 0.25 * current_level_value
                final_cells.append(current_level_value)
print("Cells:")
for final in final_cells:
    print(f" - {final}")
    total_fire += int(final)
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")