egg_size = input()
egg_color = input()
portions_count = int(input())
portion_cost = int()
if egg_size == "Large":
    if egg_color == "Red":
        portion_cost = 16
    elif egg_color == "Green":
        portion_cost = 12
    else:
        portion_cost = 9
elif egg_size == "Medium":
    if egg_color == "Red":
        portion_cost = 13
    elif egg_color == "Green":
        portion_cost = 9
    else:
        portion_cost = 7
else:
    if egg_color == "Red":
        portion_cost = 9
    elif egg_color == "Green":
        portion_cost = 8
    else:
        portion_cost = 5
total_cost = portion_cost * portions_count
total_cost = total_cost * 0.65
print(f"{total_cost:.2f} leva.")