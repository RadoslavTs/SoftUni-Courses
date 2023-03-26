from itertools import permutations


def possible_permutations(item):
    for el in list(permutations(item)):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]