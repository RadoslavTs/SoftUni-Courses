first_number = int(input())
second_number = int(input())
magic_number = int(input())
combination_found = False
combination_number = 0
for combination in range(first_number, second_number + 1):
    for combination2 in range(first_number, second_number + 1):
        combination_number += 1
        if combination + combination2 == magic_number:
            combination_found = True
            break
    if combination_found:
        break
if combination_found:
    print(f"Combination N:{combination_number} ({combination} + {combination2} = {magic_number})")
else:
    print(f"{combination_number} combinations - neither equals {magic_number}")
