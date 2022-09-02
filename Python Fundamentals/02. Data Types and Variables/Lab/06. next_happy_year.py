initial_year = int(input())
happy_year_flag = False
while not happy_year_flag:
    initial_year = str(initial_year)
    if int(initial_year[0]) != int(initial_year[1]) and int(initial_year[0]) != int(initial_year[2]) \
            and int(initial_year[0]) != int(initial_year[3]) and int(initial_year[1]) != int(initial_year[2]) \
            and int(initial_year[1]) != int(initial_year[3]) and int(initial_year[2]) != int(initial_year[3]):
        happy_year_flag = True
        initial_year = int(initial_year)
        break
    initial_year = int(initial_year)
    initial_year += 1
if happy_year_flag:
    print(initial_year)