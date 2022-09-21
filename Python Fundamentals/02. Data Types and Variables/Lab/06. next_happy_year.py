year = int(input())
happy_year_flag = False
while not happy_year_flag:
    year += 1
    set_year = set()
    for sequence in range(len(str(year))):
        set_year.add(str(year)[sequence])
    happy_year_flag = len(set_year) == len(str(year))
print(year)