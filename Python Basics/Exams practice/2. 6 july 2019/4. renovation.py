from math import ceil
wall_height = int(input())
wall_width = int(input())
exclusion_area = int(input())
surface_are_painted = input()
total_area = wall_height * wall_width * 4
exclusion_area = total_area * exclusion_area / 100
surface_to_paint = total_area - exclusion_area
tired_flag = False
remaining_surface_to_paint = surface_to_paint
while surface_are_painted != "Tired!":
    remaining_surface_to_paint -= int(surface_are_painted)
    if remaining_surface_to_paint <= 0:
        break
    surface_are_painted = input()
    if surface_are_painted == "Tired!":
        tired_flag = True
if tired_flag:
    print(f"{remaining_surface_to_paint:.0f} quadratic m left.")
elif remaining_surface_to_paint < 0:
    print(f"All walls are painted and you have {abs(remaining_surface_to_paint):.0f} l paint left!")
else:
    print("All walls are painted! Great job, Pesho!")