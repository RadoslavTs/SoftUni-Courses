number = int(input())
if number == 1:
    print("  |")
    print("* | *")
else:
    for i in range(number + 1):
        if i == 0:
            print(" " * (number + 1) + "|")
        else:
            print(" " * (number - i) + "*" * i + " | " + "*" * i)
