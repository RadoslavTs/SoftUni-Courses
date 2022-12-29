visitor_count = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0
training = 0
eating = 0
for sequence in range(visitor_count):
    activity = input()
    if activity == "Back":
        back += 1
        training += 1
    elif activity == "Chest":
        chest += 1
        training += 1
    elif activity == "Legs":
        legs += 1
        training += 1
    elif activity == "Abs":
        abs += 1
        training += 1
    elif activity == "Protein shake":
        protein_shake += 1
        eating += 1
    else:
        protein_bar += 1
        eating += 1
training_perc = training / visitor_count * 100
eating_perc = eating / visitor_count * 100
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{training_perc:.2f}% - work out")
print(f"{eating_perc:.2f}% - protein")