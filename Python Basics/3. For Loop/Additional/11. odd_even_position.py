import sys
count = int(input())
odd_sum = int()
odd_min = 1000000000.0
odd_max = -1000000000.0
even_sum = int()
even_min = 1000000000.0
even_max = -1000000000.0
for sequence in range(1, count + 1):
    number = float(input())
    if sequence % 2 != 0:
        odd_sum += number
        if number < odd_min:
            odd_min = number
        if number > odd_max:
            odd_max = number
    else:
        even_sum += number
        if number < even_min:
            even_min = number
        if number > even_max:
            even_max = number
print(f"OddSum={odd_sum:.2f},")
if odd_min == 1000000000.0:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -1000000000.0:
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_min == 1000000000.0:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == -1000000000.0:
    print("EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
