input_year = int(input())
check_set = set()
happy_year_flag = False
while not happy_year_flag:
    input_year += 1
    for sequence in range(len(str(input_year))):
        check_set.add(str(input_year)[sequence])
    if len(str(input_year)) == len(check_set):
        happy_year_flag = True
    check_set = set()
print(input_year)
