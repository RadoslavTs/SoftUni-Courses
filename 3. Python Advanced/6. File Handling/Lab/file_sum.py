data = open('text.txt', 'r')

sum = 0
for lien in data:
    sum += int(lien)

print(sum)