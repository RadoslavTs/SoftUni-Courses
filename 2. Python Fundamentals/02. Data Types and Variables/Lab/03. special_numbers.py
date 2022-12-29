number = int(input())
for sequence in range(1, number + 1):
    digits_sum = 0
    digits = sequence
    while digits > 0:
        digits_sum += digits % 10
        digits = int(digits / 10)
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        print(f"{sequence} -> True")
    else:
        print(f"{sequence} -> False")
