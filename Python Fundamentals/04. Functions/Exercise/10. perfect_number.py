def perfect(x):
    current_sum = 0
    for sequence in range(1, int(x)):
        if int(x) % sequence == 0:
            current_sum += sequence
    if current_sum == int(x):
        return "We have a perfect number!"
    return "It's not so perfect."


number = input()
print(perfect(number))