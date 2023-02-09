with open('text.txt', 'r') as file:
    current_result = file.readlines()

symbols_to_replace = ['-', ',', '.', '!', '?']

for line in range(0, len(current_result), 2):

    for symbol in symbols_to_replace:
        current_result[line] = current_result[line].replace(symbol, "@")

    print(*current_result[line].split()[::-1], sep=' ')
