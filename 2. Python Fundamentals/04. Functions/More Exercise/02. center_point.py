import math


def closest(x, y, z, p):
    point_one_distance = math.sqrt((x * x) + (y * y))
    point_two_distance = math.sqrt((z * z) + (p * p))
    if point_one_distance <= point_two_distance:
        print(f"({math.floor(x)}, {math.floor(y)})")
    else:
        print(f"({math.floor(z)}, {math.floor(p)})")


closest(float(input()), float(input()), float(input()), float(input()))