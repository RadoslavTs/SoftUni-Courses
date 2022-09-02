stadium_capacity = int(input())
total_fans = int(input())
fans_a_per = float()
fans_b_per = float()
fans_v_per = float()
fans_g_per = float()
total_a = int()
total_b = int()
total_v = int()
total_g = int()
for sequence in range(total_fans):
    sector = input()
    if sector == "A":
        total_a += 1
    elif sector == "B":
        total_b += 1
    elif sector == "V":
        total_v += 1
    else:
        total_g += 1
capacity_fill_per = total_fans / stadium_capacity * 100
fans_a_per = total_a / total_fans * 100
fans_b_per = total_b / total_fans * 100
fans_v_per = total_v / total_fans * 100
fans_g_per = total_g / total_fans * 100
print(f"{fans_a_per:.2f}%")
print(f"{fans_b_per:.2f}%")
print(f"{fans_v_per:.2f}%")
print(f"{fans_g_per:.2f}%")
print(f"{capacity_fill_per:.2f}%")
