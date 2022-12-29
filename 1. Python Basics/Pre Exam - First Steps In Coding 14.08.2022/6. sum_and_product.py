number = int(input())
valid_combination_flag = False
multiply = 0
sum = 0
for sequence_a in range(1, 10):
    for sequence_b in range(9, sequence_a - 1, -1):
        for sequence_c in range(0, 10):
            for sequence_d in range(9, sequence_c - 1, -1):
                multiply = sequence_a * sequence_b * sequence_c * sequence_d
                sum = sequence_a + sequence_b + sequence_c + sequence_d
                if sequence_a + sequence_b + sequence_c + sequence_d == sequence_a * sequence_b * sequence_c * sequence_d and number % 10 == 5:
                    code_a = str(sequence_a)
                    code_b = str(sequence_b)
                    code_c = str(sequence_c)
                    code_d = str(sequence_d)
                    code = code_a + code_b + code_c + code_d
                    print(int(code))
                    valid_combination_flag = True
                    break
                elif multiply // sum == 3 and number % 3 == 0:
                    print(sequence_d * 1000 + sequence_c * 100 + sequence_b * 10 + sequence_a)
                    valid_combination_flag = True
                    break
            if valid_combination_flag:
                break
        if valid_combination_flag:
            break
    if valid_combination_flag:
        break
if not valid_combination_flag:
    print("Nothing found")