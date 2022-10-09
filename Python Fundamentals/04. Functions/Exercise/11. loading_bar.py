def loading(x):
    percentage_count = x / 10
    dots_count = 10 - (x / 10)
    if x == 100:
        print("100% Complete!")
        print(f"[{int(percentage_count) * '%'}{int(dots_count) * '.'}]")
    if x < 100:
        print(f"{x}% [{int(percentage_count) * '%'}{int(dots_count) * '.'}]")
        print("Still loading...")


loading(int(input()))