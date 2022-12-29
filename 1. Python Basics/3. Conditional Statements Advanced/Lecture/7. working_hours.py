time = int(input())
day = input()
if day == "Sunday" or time < 10 or time > 18:
    print("closed")
else:
    print("open")
