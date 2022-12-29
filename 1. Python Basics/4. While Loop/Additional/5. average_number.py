number = int(input())
sum = 0
for sequence in range(number):
    additives = int(input())
    sum += additives
print(f"{(sum / number):.2f}")