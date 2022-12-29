group_number = int(input())
musala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
for sequence in range(group_number):
    people_per_group = int(input())
    if people_per_group <= 5:
        musala_count += people_per_group
    elif people_per_group <= 12:
        monblan_count += people_per_group
    elif people_per_group <= 25:
        kilimanjaro_count += people_per_group
    elif people_per_group <= 40:
        k2_count += people_per_group
    else:
        everest_count += people_per_group
total_people = musala_count + monblan_count + kilimanjaro_count + k2_count + everest_count
print(f"{((musala_count / total_people) * 100):.2f}%")
print(f"{((monblan_count / total_people) * 100):.2f}%")
print(f"{((kilimanjaro_count / total_people) * 100):.2f}%")
print(f"{((k2_count / total_people) * 100):.2f}%")
print(f"{((everest_count / total_people) * 100):.2f}%")
