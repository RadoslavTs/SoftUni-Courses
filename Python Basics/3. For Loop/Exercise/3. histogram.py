quantity = int(input())
p1 = int()
p2 = int()
p3 = int()
p4 = int()
p5 = int()
for sequence in range(quantity):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number < 400:
        p2 += 1
    elif 400 <= number < 600:
        p3 += 1
    elif 600 <= number < 800:
        p4 += 1
    else:
        p5 += 1
p1 = p1 / quantity * 100
p2 = p2 / quantity * 100
p3 = p3 / quantity * 100
p4 = p4 / quantity * 100
p5 = p5 / quantity * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

