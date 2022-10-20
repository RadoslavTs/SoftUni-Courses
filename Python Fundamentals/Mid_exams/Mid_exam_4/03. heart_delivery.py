neighbourhood = list(map(int, input().split("@")))
command = input()
last_jump_length = 0
all_house_valentine = True
no_valentines_count = 0
while command != "Love!":
    command_list = command.split()
    action = command_list[0]
    jump_length = int(command_list[1]) + last_jump_length
    if jump_length > len(neighbourhood) - 1:
        jump_length = 0
    if neighbourhood[jump_length] == 0:
        print(f"Place {jump_length} already had Valentine's day.")
    elif neighbourhood[jump_length] > 2:
        neighbourhood[jump_length] -= 2
    elif neighbourhood[jump_length] == 2:
        neighbourhood[jump_length] -= 2
        print(f"Place {jump_length} has Valentine's day.")
    last_jump_length = jump_length
    command = input()
print(f"Cupid's last position was {last_jump_length}.")
for check in neighbourhood:
    if check != 0:
        all_house_valentine = False
        no_valentines_count += 1
if all_house_valentine:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {no_valentines_count} places.")

