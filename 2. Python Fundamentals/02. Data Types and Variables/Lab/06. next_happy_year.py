year = int(input())
happy_year_flag = False
while not happy_year_flag:
    year += 1
    set_year = set()
    for sequence in range(len(str(year))):
        set_year.add(str(year)[sequence])
    happy_year_flag = len(set_year) == len(str(year))
print(year)

# from itertools import permutations
#
# number = tuple(map(int, input()))
# myperm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(number))
# for digits in list(myperm):
#     if digits > number:
#         result = ''.join(str(x) for x in digits)
#         print(result)
#         break