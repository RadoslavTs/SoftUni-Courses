def check(x, y, z):
    if x < 0 or y < 0 or z < 0:
        print("negative")
    elif x == 0 or y == 0 or z == 0:
        print("zero")
    elif x > 0 or y > 0 or z > 0:
        print("positive")


check(int(input()), int(input()), int(input()))
