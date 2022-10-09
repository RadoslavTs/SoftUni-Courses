def check(x, y):
    if x == "int":
        print(int(y) * 2)
    elif x == "real":
        print(f"{(float(y) * 1.5):.2f}")
    else:
        print(f"${y}$")


check(input(), input())