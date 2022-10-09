sum_of_even = int()
sum_of_odds = int()


def sum_finder(x):
    if x % 2 == 0:
        sum_of_even += x
    else:
        sum_of_odds += x


input_string = input()
for sequene in range(len(input_string)):
    if int(input_string[sequene]) % 2 == 0:
        sum_of_even += int(input_string[sequene])
    else:
        sum_of_odds += int(input_string[sequene])
print(f"Odd sum = {sum_of_odds}, Even sum = {sum_of_even}")