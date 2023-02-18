from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

patches = 0
bandages = 0
medkits = 0


while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    current_sum = current_textile + current_medicament
    if current_sum == 30:
        patches += 1
    elif current_sum == 40:
        bandages += 1
    elif current_sum == 100:
        medkits += 1
    elif current_sum > 100:
        remaining = current_sum - 100
        medkits += 1
        current_medicament = medicaments.pop()
        current_medicament += remaining
        medicaments.append(current_medicament)
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

created_dict = {
    "Patch": patches,
    "Bandage": bandages,
    "MedKit": medkits
}

for item, qty in sorted(created_dict.items(), key=lambda x: (-x[1], x[0])):
    if qty:
        print(f"{item} - {qty}")

reversed_medicaments = []
if medicaments:
    for _ in range(len(medicaments)-1, -1, -1):
        reversed_medicaments.append(medicaments[_])

if reversed_medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed_medicaments)}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")