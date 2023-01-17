first_size, second_size = (int(x) for x in input().split())
first_set = set()
second_set = set()
for first_sequence in range(first_size):
    first_set.add(input())
for second_sequence in range(second_size):
    second_set.add(input())
resulting_set = first_set.intersection(second_set)
for result in resulting_set:
    print(result)
