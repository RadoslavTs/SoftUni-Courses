climbers_groups_count = int(input())
musala = int()
monblan = int()
kilimanjaro = int()
k2 = int()
everest = int()
total_climbers = int()
musala_perc = float()
monblan_perc = float()
kilimanjaro_perc = float()
k2_perc = float()
everest_perc = float()
total_climbers = int()

for sequence in range(climbers_groups_count):
    climbers_per_group = int(input())
    if climbers_per_group <= 5:
        musala += climbers_per_group
        total_climbers += climbers_per_group
    elif climbers_per_group <= 12:
        monblan += climbers_per_group
        total_climbers += climbers_per_group
    elif climbers_per_group <= 25:
        kilimanjaro += climbers_per_group
        total_climbers += climbers_per_group
    elif climbers_per_group <= 40:
        k2 += climbers_per_group
        total_climbers += climbers_per_group
    else:
        everest += climbers_per_group
        total_climbers += climbers_per_group
musala_perc = musala / total_climbers * 100
monblan_perc = monblan / total_climbers * 100
kilimanjaro_perc = kilimanjaro / total_climbers * 100
k2_perc = k2 / total_climbers * 100
everest_perc = everest / total_climbers * 100
print(f"{musala_perc:.2f}%")
print(f"{monblan_perc:.2f}%")
print(f"{kilimanjaro_perc:.2f}%")
print(f"{k2_perc:.2f}%")
print(f"{everest_perc:.2f}%")

