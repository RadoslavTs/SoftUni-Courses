number = int(input())
even_set = set()
odd_set = set()
for sequence in range(1, number+1):
    name = input()
    ascii_value = 0
    for letter in name:
        ascii_value += ord(letter)
    if (ascii_value // sequence) % 2 == 0:
        even_set.add((ascii_value // sequence))
    else:
        odd_set.add((ascii_value // sequence))
sum_even = 0
sum_odd = 0
resulting_set = ()
for value in even_set:
    sum_even += value
for value in odd_set:
    sum_odd += value
if sum_odd == sum_even:
    resulting_set = even_set.union(odd_set)
elif sum_odd > sum_even:
    resulting_set = odd_set.difference(even_set)
else:
    resulting_set = even_set.symmetric_difference(odd_set)
resulting_string = ', '.join(map(lambda result: f'{result}', resulting_set))
print(resulting_string)
