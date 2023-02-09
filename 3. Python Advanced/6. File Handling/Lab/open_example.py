with open('text.txt', 'r') as file:
    data = file.readlines()
    sum = 0
    for line in data:
        current = line.split()
        sum += int(current[0])

print(sum)
