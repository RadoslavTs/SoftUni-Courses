def my_func(*numbers):
    negatives = []
    positives = []
    for number in numbers[0]:
        if number < 0:
            negatives.append(number)
    for number in numbers[0]:
        if number >= 0:
            positives.append(number)
    return sum(negatives), sum(positives)


input_numbers = [int(x) for x in input().split()]
negatives, positives = my_func(input_numbers)
print(negatives)
print(positives)
if abs(negatives) < abs(positives):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
