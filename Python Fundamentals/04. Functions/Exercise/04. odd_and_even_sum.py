def sum_finder(x):
    sum_of_even = int()
    sum_of_odds = int()
    for sequence in range(len(x)):
        if int(x[sequence]) % 2 == 0:
            sum_of_even += int(x[sequence])
        else:
            sum_of_odds += int(x[sequence])
    return f"Odd sum = {sum_of_odds}, Even sum = {sum_of_even}"


input_string = input()
print(sum_finder(input_string))