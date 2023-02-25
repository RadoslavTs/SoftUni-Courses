def print_rhombus(num):
    for x in range(num):
        spaces = num - x - 1
        stars = x + 1
        print(f"{' ' * spaces}{'* ' * stars}")

    for x in range(num-2, -1, -1):
        spaces = num - x - 1
        stars = x + 1
        print(f"{' ' * spaces}{'* ' * stars}")


size = int(input())
print_rhombus(size)
