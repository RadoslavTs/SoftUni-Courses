import math


def longest(a, b, c, d, e, f, g, h):
    line_one = math.sqrt(((c - a) ** 2) + ((d-b) ** 2))
    line_two = math.sqrt(((g - e) ** 2) + ((h - f) ** 2))
    if line_one >= line_two:
        if math.sqrt(c * c + d * d) < math.sqrt(a * a + b * b):
            print(f"({math.floor(c)}, {math.floor(d)})({math.floor(a)}, {math.floor(b)}")
        else:
            print(f"({math.floor(a)}, {math.floor(b)})({math.floor(c)}, {math.floor(d)}")
    else:
        if math.sqrt(g * g + h * h) < math.sqrt(e * e + f * f):
            print(f"({math.floor(g)}, {math.floor(h)})({math.floor(e)}, {math.floor(f)})")
        else:
            print(f"({math.floor(e)}, {math.floor(f)})({math.floor(g)}, {math.floor(h)})")


longest(float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()))


