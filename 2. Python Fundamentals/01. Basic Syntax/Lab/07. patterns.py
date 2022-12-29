number = int(input())
for sequence in range(1, number + 1):
    for sequence_two in range(0, sequence):
        print("*", end = "")
    print()
for sequence in range(number -1, 0, -1):
    for sequence_two in range(0, sequence):
        print("*", end = "")
    print()