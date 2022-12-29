number = int(input())
for sequence in range(1, number + 1):
    if sequence == 1:
        print("+ " + "- " * (number - 2) + "+")
    if sequence == number:
        print("+ " + "- " * (number - 2) + "+")
    if sequence != 1 and sequence != number:
        print("| " + "- " * (number - 2) + "|")
