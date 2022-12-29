date = input().split("-")
year, month, day = int(date[0]), int(date[1]), int(date[2])
if year == 2018 and month == 8 and day == 26:
    print("Today date")
elif day < 26 and month < 8 and year <= 2018:
    print("Passed")
else:
    for years in range(2018, year+1):
        for months in range()

