painted_eggs = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs = 0
max_eggs_color = ""
for sequence in range(painted_eggs):
    egg_color = input()
    if egg_color == "red":
        red_eggs += 1
    elif egg_color == "orange":
        orange_eggs += 1
    elif egg_color == "blue":
        blue_eggs += 1
    else:
        egg_color == "green"
        green_eggs += 1
if red_eggs > orange_eggs and red_eggs > blue_eggs and red_eggs > green_eggs:
    max_eggs = red_eggs
    max_eggs_color = "red"
elif orange_eggs > red_eggs and orange_eggs > blue_eggs and orange_eggs > green_eggs:
    max_eggs = orange_eggs
    max_eggs_color = "orange"
elif blue_eggs > red_eggs and blue_eggs > orange_eggs and blue_eggs > green_eggs:
    max_eggs = blue_eggs
    max_eggs_color = "blue"
else:
    max_eggs = green_eggs
    max_eggs_color = "green"
print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {max_eggs_color}")
