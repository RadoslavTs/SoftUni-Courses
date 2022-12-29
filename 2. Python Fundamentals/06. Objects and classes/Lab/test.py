count = int(input())
print((" " * (count + 1)) + "|")
for sequence in range(1, count+1):
    print((" " * (count - sequence) + "*" * sequence + " " + "|" + " " + "*" * sequence))