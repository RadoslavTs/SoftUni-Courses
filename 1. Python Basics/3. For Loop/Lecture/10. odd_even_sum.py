number = int(input())
odd_sum = 0
even_sum = 0
for sequence in range(number):
    from_human = int(input())
    if sequence % 2 == 0:
        even_sum += from_human
    else:
        odd_sum += from_human
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    difference = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {difference}")
