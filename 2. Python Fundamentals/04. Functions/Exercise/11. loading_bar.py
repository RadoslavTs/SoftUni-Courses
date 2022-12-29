def loading(x):
    percentage_count = x / 10
    dots_count = 10 - (x / 10)
    if x == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    if x < 100:
        return f"{x}% [{int(percentage_count) * '%'}{int(dots_count) * '.'}]\nStill loading..."


number = int(input())
print(loading(number))